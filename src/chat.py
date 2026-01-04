from langchain_ollama import ChatOllama

qwen = ChatOllama(
    model="qwen3:8b",
    name="qwen3:8b",
    temperature=0.8,
    reasoning=False
)

deepseek = ChatOllama(
    model="deepseek-r1:8b",
    name="deepseek-r1:8b",
    temperature=0.8,
    reasoning=False
)

llama = ChatOllama(
    model="llama3.1:8b",
    name="llama3.1:8b",
    temperature=0.8,
    reasoning=False
)

all_models = [
    qwen,
    deepseek,
    llama
]
