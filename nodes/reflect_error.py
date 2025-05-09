from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from utils.state_schema import AgentState
from prompts.error_reflect import reflect_prompt
from Schema.init_schema import ReflectErrorSchema

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini").bind_tools(
    tools=[ReflectErrorSchema],
    tool_choice="ReflectErrorSchema"
)

def reflect_on_error(state: AgentState) -> AgentState:
    # Step 1: Flatten code list to string for input prompt
    formatted_code = "\n\n".join([
        f"{state['code'][i]}:\n{state['code'][i + 1]}"
        for i in range(0, len(state["code"]), 2)
    ])

    prompt = reflect_prompt.format(
        task=state["prompt"],
        code=formatted_code,
        requirements=state["requirements"],
        explanation=state["explanation"],
        error=state["error"]
    )

    result = llm.invoke(prompt)

    if not result.tool_calls:
        raise ValueError("No tool call was returned by the LLM.")

    tool_args = result.tool_calls[0]["args"]

    return {
        **state,
        "code": tool_args.get("code", []),  # <- expecting flat list
        "explanation": tool_args.get("explanation", ""),
        "requirements": tool_args.get("requirements", None),
        "step_count": state["step_count"] + 1
    }