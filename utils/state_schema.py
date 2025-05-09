from typing import TypedDict, Optional, Union, List
from typing_extensions import NotRequired

class AgentState(TypedDict):
    prompt: str
    code: NotRequired[List[str]]
    explanation: NotRequired[str]
    requirements: NotRequired[Optional[str]]
    output: NotRequired[str]
    error: NotRequired[str]
    step_count: NotRequired[int]
    max_steps: NotRequired[int]
    final: NotRequired[Union[str, None]]