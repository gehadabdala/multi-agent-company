from pydantic import BaseModel, Field


class DeveloperResponse(BaseModel):
    code: str = Field(description="Generated source code.")
