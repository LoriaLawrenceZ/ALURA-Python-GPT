from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
model = "gpt-4"

def categoriza_produto(nome_produto, lista_categorias_possiveis):
    system_prompt = f"""
        Você é um categorizador de produtos.
        Você deve assumir as categorias presentes na lista abaixo.
    
        # Lista de Categorias Válidas
            {lista_categorias_possiveis.split(",")}
    
        # Formato da Saída
        Produto: Nome do Produto
        Categoria: apresente a categoria do produto
    
        # Exemplo de Saída
        Produto: Escova elétrica com recarga solar
        Categoria: Eletrônicos Verdes
    """

    response = client.chat.completions.create(
        messages = [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": nome_produto
            }
        ],
        model = model,
        temperature = 0.5,
        max_completion_tokens = 256
    )

    return print(response.choices[0].message.content)


categorias_validas = input("Informe as categorias válidas, separando por vírgula: ")

while True:
    nome_produto = input("Informe o nome do produto: ")
    texto_resposta = categoriza_produto(nome_produto, categorias_validas)
    print(texto_resposta)