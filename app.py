from flask import Flask, render_template, request, Response
from openai import OpenAI
from dotenv import load_dotenv
import os
from time import sleep
from helpers import *

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
model = "gpt-4"

app = Flask(__name__)
app.secret_key = 'alura'

contexto = carrega("dados/ecomart.txt")


def bot(prompt):
    maximo_tentativas = 1
    repeticao = 0

    while True:
        try:
            system_prompt = f"""
            Você é um chatbot de atendimento a clientes de um e-commerce. 
            Você não deve responder perguntas que não sejam dados do e-commerce informado!
            
            Você deve gerar respostas utilizando o contexto abaixo
            
            # Contexto
            {contexto}
            """
            response = client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": system_prompt
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=1,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
                model=model)
            return response
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
    texto_resposta = response.choices[0].message.content
    return texto_resposta


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
