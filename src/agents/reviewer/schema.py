from pydantic import BaseModel, Field


class ReviewerDecision(BaseModel):

    approved: bool = Field(description="Whether the generated code is approved.")

    feedback: str = Field(description="Review feedback.")

    score: int = Field(ge=0, le=10, description="Quality score from 0 to 10.")
