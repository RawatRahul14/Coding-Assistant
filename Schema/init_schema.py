from pydantic import BaseModel, Field
from typing import Optional, List

class GenerateCodeSchema(BaseModel):
    code: List[str] = Field(
        description = "List alternating between code section names and corresponding code strings."
    )
    explanation: List[str] = Field(
        description="A concise explanation of the code logic."
    )
    requirements: Optional[str] = Field(
        default = None,
        description = "Shell commands to install any required libraries (if applicable).")
    
class ReflectErrorSchema(BaseModel):
    code: List[str] = Field(
        description="A corrected version of the provided Python code."
    )
    explanation: str = Field(
        description="A clear explanation of how the corrected code works. This should be error-free."
    )
    requirements: Optional[str] = Field(
        default = None, 
        description = "Updated or confirmed installation requirements (if any)."
    )