from typing import TypedDict, Optional, Union
from typing_extensions import NotRequired

class AgentState(TypedDict):
    prompt: str
    code: NotRequired[str]
    explanation: NotRequired[str]
    requirements: NotRequired[Optional[str]]
    output: NotRequired[str]
    error: NotRequired[str]
    step_count: NotRequired[int]
    max_steps: NotRequired[int]
    final: NotRequired[Union[str, None]]