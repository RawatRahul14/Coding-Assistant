from typing import TypedDict, Union

class AgentState(TypedDict):
    prompt: str
    code: str
    output: str
    error: str
    step_count: int
    max_steps: int
    final: Union[str, None]