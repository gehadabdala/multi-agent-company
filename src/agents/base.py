from abc import ABC, abstractmethod  # ABC=Abstract Base Class
from shared.state import AgentState


class BaseAgent(ABC):
    """
    Abstract base class for all agents.
    """

    @abstractmethod  # لازم اعمل invoke لو هورث من الكلاس دا
    def invoke(
        self,
        state: AgentState,
    ) -> AgentState:
        """
        Execute the agent logic.
        """
        pass
