from openai import OpenAI
from dotenv import load_dotenv
import os
from time import sleep
from helpers import *
from selecionar_persona import *
import json

load_dotenv()

cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
modelo = "gpt-4-1106-preview"
contexto = carrega("dados/ecomart.txt")

def criar_thread():
    return cliente.beta.threads.create()
    

def criar_assistente():
    assistente = cliente.beta.assistants.create(
    name="Atendente EcoMart",
    instructions = f"""
        Você é um chatbot de atendimento a clientes de um e-commerce. 
        Você não deve responder perguntas que não sejam dados do ecommerce informado!
        Além disso, acesse os arquivos associados a você e a thread para responder as perguntas.
        
    """,
    model = modelo
)
    return assistente

