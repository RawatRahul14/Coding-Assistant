from langchain_openai import ChatOpenAI
from utils.state_schema import AgentState
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model = "gpt-4o-mini")

def generate_code(state: AgentState,
                  llm = llm):
    prompt = f'Write Python code to: {state["prompt"]}'
    result = llm.invoke(prompt)
    return {
        **state,
        "code": result.content
    }