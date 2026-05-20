from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM
from langserve import add_routes
import uvicorn

app=FastAPI(
    title="LangChain Server",
    version="1.0",
    description="Simple API Server"
)

# TinyLlama model
llm=OllamaLLM(model="tinyllama")

# Prompt
prompt=ChatPromptTemplate.from_template(
    "Write me a poem about {topic} for a 5 year old child"
)

# Route
add_routes(
    app,
    prompt | llm,
    path="/poem"
)

if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)