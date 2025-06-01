from fastapi import FastAPI
from app.agents.base_agent import get_agent

app = FastAPI()

@app.get("/")
def health_check():
    return {"message": "Agent AI is live with TinyLLaMA!"}

@app.get("/run")
def run_agent(query: str):
    agent = get_agent()
    response = agent.run(query)
    return {"response": response}
