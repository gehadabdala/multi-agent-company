from pydantic import BaseModel, Field

from shared.enums import AgentType


class SupervisorDecision(BaseModel):
    """
    Structured output returned by the Supervisor Agent.
    """

    next_agent: AgentType = Field(
        description="The next agent that should handle the user's request."
    )
