from pydantic import BaseModel, Field
from typing import Optional

class GenerateCodeSchema(BaseModel):
    code: str = Field(description = "The complete runnable code inside a Python code block.")
    explanation: str = Field(description = "A brief explanation of the code logic.")
    requirements: Optional[str] = Field(default = None,
                                        description = "Installation commands for required libraries, if any.")