from openai import OpenAI
from dotenv import load_dotenv
import os
from time import sleep
from helpers import *
from selecionar_persona import *

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
model = "gpt-4"
context = carrega("dados/dados_ecomart.txt")

def criar_thread():
    return client.beta.threads.create()

def criar_assitente():
    assistente = client.beta.assistants.create(
        name="Atendente EcoMart",
        instructions = f"""
            Você é um chatbot de atendimento a clientes de um e-commerce. 
            Você não deve responder perguntas que não sejam dados do ecommerce informado!
            Além disso, adote a persona abaixo para responder ao cliente.
            
            ## Contexto
            {context}
            
            ## Persona
            {personas["neutro"]}
        """,
        model = model,
    )

    return assistente
