from openai import OpenAI
from dotenv import load_dotenv
import os
import openai

load_dotenv()

# errado -> client = OpenAI(api_key=os.getenv("ALURA"))
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# errado -> model = "gpt-4-alura"
model = "gpt-4"

def carrega(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, "r") as arquivo:
            dados = arquivo.read()
            return dados
    except IOError as e:
        print(f"Error: {e}")

def salva(nome_do_arquivo, conteudo):
    try:
        with open(nome_do_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(conteudo)
    except IOError as e:
        print(f"Erro ao salvar arquivo: {e}")

def analisador_sentimentos(produto):
    system_prompt = f"""
        Você é um analisador de sentimentos de avaliações de produtos.
        Escreva um parágrafo com até 50 palavras resumindo as avaliações e 
        depois atribua qual o sentimento geral para o produto.
        Identifique também 3 pontos fortes e 3 pontos fracos identificados a partir das avaliações.

        # Formato de Saída

        Nome do Produto:
        Resumo das Avaliações:
        Sentimento Geral: [utilize aqui apenas Positivo, Negativo ou Neutro]
        Ponto fortes: lista com três bullets
        Pontos fracos: lista com três bullets
    """

    user_prompt = carrega(f"dados/avaliacoes-{produto}.txt")
    print(f"Iniciou a análise de sentimentos do produto {produto}")

    lista_mensagens = [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": user_prompt
        }
    ]

    try:
        response = client.chat.completions.create(
            messages = lista_mensagens,
            model = model
        )

        texto_resposta = response.choices[0].message.content
        salva(f"dados/analise-{produto}.txt", texto_resposta)

    except openai.AuthenticationError as authe:
        print(f"Erro de Autenticação: {authe}")
    except openai.APIError as apie:
        print(f"Erro de API: {apie}")

lista_de_produtos = ["Camisetas de algodão orgânico", "Jeans feitos com materiais reciclados", "Maquiagem mineral"]
for produto in lista_de_produtos:
    analisador_sentimentos(produto)
