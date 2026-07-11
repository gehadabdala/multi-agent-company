from pydantic import BaseModel, Field


class PlannerStep(BaseModel):
    description: str = Field(description="Description of the implementation step.")


class PlannerResponse(BaseModel):
    steps: list[PlannerStep]
