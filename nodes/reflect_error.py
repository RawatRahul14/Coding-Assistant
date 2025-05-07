from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

def reflect_on_error(state):
    prompt = f"""
                The code:\n
                {state['code']}\n\n
                
                Raised this error:\n
                {state['error']}\n
                Fix the code and output only the new corrected code."""
    result = llm.invoke(prompt)
    return {
        **state,
        "code": result.content,
        "step_count": state["step_count"] + 1
    }