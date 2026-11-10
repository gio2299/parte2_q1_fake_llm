from fastapi import FastAPI
from pydantic import BaseModel
from langchain_core.language_models.fake import FakeListLLM

app = FastAPI(title="Chatbot com Fake LLM")

# o Fake LLM devolve as respostas da lista, em ordem, sem usar nenhum modelo real
llm = FakeListLLM(responses=[
    "Olá! Como posso ajudar?",
    "Sou um chatbot de teste.",
    "Esta é uma resposta simulada.",
    "Até logo!",
])


class Entrada(BaseModel):
    texto: str


@app.post("/chat")
def chat(entrada: Entrada):
    resposta = llm.invoke(entrada.texto)
    return {"pergunta": entrada.texto, "resposta": resposta}