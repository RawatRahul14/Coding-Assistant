from langchain_openai import ChatOpenAI
from utils.state_schema import AgentState
from langchain_core.runnables import RunnableLambda
from prompts.generation_prompt import generate_prompt
from dotenv import load_dotenv
from Schema.init_schema import GenerateCodeSchema

load_dotenv()

llm = ChatOpenAI(model = "gpt-4o-mini").bind_tools(tools = [GenerateCodeSchema],
                                                   tool_choice = "GenerateCodeSchema")

def generate_code(state: AgentState) -> AgentState:

    prompt = generate_prompt.format(task = state["prompt"])
    result = llm.invoke(prompt)

    if not result.tool_calls:
        raise ValueError("No tool call was made. Make sure your prompt is designed to invoke the tool.")

    tool_args = result.tool_calls[0]["args"]

    return {
        **state,
        "code": tool_args.get("code", ""),
        "explanation": tool_args.get("explanation", ""),
        "requirements": tool_args.get("requirements", None)
    }

generate_code_chain = RunnableLambda(generate_code)