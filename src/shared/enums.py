from enum import Enum


class AgentType(str, Enum):
    """
    Represents all available agents in the system.
    """

    SUPERVISOR = "supervisor"

    PLANNER = "planner"

    DEVELOPER = "developer"

    REVIEWER = "reviewer"

    DIRECT_ANSWER = "direct_answer"
