from langgraph.graph import StateGraph, END
from utils.state_schema import AgentState
from nodes.generate_code import generate_code
from nodes.test_code import test_code
from nodes.reflect_error import reflect_on_error

def should_continue(state: AgentState) -> str:
    if state["final"] == "success":
        return "__end__"
    if state["step_count"] >= state["max_steps"]:
        return "give_up"
    return "reflect_on_error"

def build_graph():
    graph = StateGraph(AgentState)
    graph.add_node("generate_code", generate_code)
    graph.add_node("test_code", test_code)
    graph.add_node("reflect_on_error", reflect_on_error)
    graph.add_node("give_up", lambda s: {**s, "final": "failed"})

    graph.set_entry_point("generate_code")
    graph.add_edge("generate_code", "test_code")
    graph.add_conditional_edges("test_code", should_continue, {
        "reflect_on_error": "reflect_on_error",
        "give_up": "give_up",
        "__end__": END
    })
    graph.add_edge("reflect_on_error", "test_code")

    return graph.compile()