from pydantic import BaseModel

from shared.enums import AgentType


class SupervisorDecision(BaseModel):
    next_agent: AgentType
