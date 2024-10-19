from flask import Flask, render_template, request, Response
from openai import OpenAI
from dotenv import load_dotenv
import os
from time import sleep
from helpers import *
from selecionar_documento import *
from selecionar_persona import *
from assistente_ecomart import *
from tools_ecomart import minhas_funcoes

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
model = "gpt-4"

app = Flask(__name__)
app.secret_key = 'alura'

assistente = pegar_json()
thread_id = assistente["thread_id"]
assistente_id = assistente["assistant_id"]
file_ids = assistente["file_ids"]

STATUS_COMPLETED = "completed"
STATUS_REQUIRES_ACTION = "requires_action"

def bot(prompt):
    maximo_tentativas = 1
    repeticao = 0

    while True:
        try:
            personalidade = personas[selecionar_persona(prompt)]

            client.beta.threads.messages.create(
                thread_id = thread_id,
                role = "user",
                content = f"""
                Assuma, de qagora em diante, a personalidade abaixo.
                Ignore as personalidades anteriores.
                
                # Persona
                {personalidade}
                """,
                file_ids = file_ids
            )

            client.beta.threads.messages.create(
                thread_id = thread_id,
                role = "user",
                content = prompt,
                file_ids = file_ids
            )

            run = client.beta.threads.runs.create(
                thread_id = thread_id,
                assistant_id = assistente_id
            )

            while run.status != STATUS_COMPLETED:
                run = client.beta.threads.runs.retrieve(
                    thread_id = thread_id,
                    run_id = run.id
                )

                print(f"Status: {run.status}")

                if run.status == STATUS_REQUIRES_ACTION:
                    tools_acionadas = run.required_action.submit_tool_outputs.tool_calls
                    respostas_tools_acionadas = []

                    for tool in tools_acionadas:
                        nome_funcao = tool.function.name
                        funcao_escolhida = minhas_funcoes[nome_funcao]
                        argumentos = json.loads(tool.function.arguments)
                        print(argumentos)
                        resposta_funcao = funcao_escolhida(argumentos)

                        respostas_tools_acionadas.append(
                            {
                                "tool_call_id": tool.id,
                                "output": resposta_funcao
                            }
                        )

                    run = client.beta.threads.runs.submit_tool_outputs(
                        thread_id = thread_id,
                        run_id = run.id,
                        tool_outputs = respostas_tools_acionadas
                    )


            historico = list(client.beta.threads.messages.list(thread_id = thread_id).data)
            resposta = historico[0]
            return resposta

        except Exception as erro:
            repeticao += 1
            if repeticao >= maximo_tentativas:
                return "Erro no GPT: %s" % erro
            print('Erro de comunicação com OpenAI:', erro)
            sleep(1)



@app.route("/chat", methods=["POST"])
def chat():
    user_prompt = request.json["msg"]
    response = bot(user_prompt)
    texto_resposta = response.content[0].text.value
    return texto_resposta


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
