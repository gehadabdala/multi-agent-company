from langchain_core.messages import HumanMessage, SystemMessage

from agents.base import BaseAgent
from agents.planner.prompt import system_prompt
from agents.planner.schema import PlannerResponse

from services.llm import llm

from shared.models import (
    Plan,
    Step,
)

from shared.state import AgentState
from shared.enums import AgentType


class PlannerAgent(BaseAgent):

    def invoke(
        self,
        state: AgentState,
    ) -> AgentState:

        request = state["task"].request

        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=request),
        ]

        structured_llm = llm.with_structured_output(PlannerResponse)

        response = structured_llm.invoke(messages)

        state["plan"] = Plan(
            steps=[Step(description=step.description) for step in response.steps]
        )

        state["current_agent"] = AgentType.PLANNER
        state["next_agent"] = AgentType.DEVELOPER

        return state
