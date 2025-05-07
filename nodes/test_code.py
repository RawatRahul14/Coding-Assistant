from utils.state_schema import AgentState

def test_code(state: AgentState):
    try:
        local_env = {}
        exec(state["code"], {}, local_env)
        return {
            **state,
            "output": str(local_env),
            "error": "",
            "final": "success"
        }
    
    except Exception as e:
        return {
            **state,
            "output": "",
            "error": str(e),
            "final": None
        }