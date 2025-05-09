from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from utils.state_schema import AgentState
from prompts.error_reflect import reflect_prompt
from Schema.init_schema import ReflectErrorSchema

load_dotenv()

llm = ChatOpenAI(model = "gpt-4o-mini").bind_tools(tools = [ReflectErrorSchema],
                                                   tool_choice = "ReflectErrorSchema")

def reflect_on_error(state: AgentState) -> AgentState:

    prompt = reflect_prompt.format(task = state["prompt"],
                                   code = state["code"],
                                   requirements = state["requirements"],
                                   explanation = state["explanation"],
                                   error = state["error"])
    
    result = llm.invoke(prompt)

    if not result.tool_calls:
        raise ValueError("No tool call was returned by the LLM.")

    tool_args = result.tool_calls[0]["args"]

    return {
        **state,
        "code": tool_args.get("code", ""),
        "explanation": tool_args.get("explanation", ""),
        "requirements": tool_args.get("requirements", None),
        "step_count": state["step_count"] + 1
    }