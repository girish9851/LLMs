from langchain.llms import LlamaCpp
from langchain.agents import initialize_agent, Tool, AgentType

MODEL_PATH = "models/tinyllama/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf"

def get_agent():
    llm = LlamaCpp(
        model_path=MODEL_PATH,
        temperature=0.5,
        max_tokens=128,
        n_ctx=512,
        verbose=True,
        f16_kv=True,
        use_mlock=True,
        low_cpu_mem_usage=True
    )

    def echo_tool(input_text: str):
        return f"Echo: {input_text}"

    tools = [
        Tool.from_function(func=echo_tool, name="Echo", description="Echo input text")
    ]

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

    return agent
