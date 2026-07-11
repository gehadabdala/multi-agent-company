from langchain_core.messages import (
    HumanMessage,
    SystemMessage,
)

from agents.reviewer.prompt import system_prompt
from agents.reviewer.schema import ReviewerDecision

from services.llm import llm

from shared.enums import AgentType
from shared.models import Review
from shared.state import AgentState


class ReviewerAgent:

    def invoke(
        self,
        state: AgentState,
    ) -> AgentState:

        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=state["code"].content),
        ]

        structured_llm = llm.with_structured_output(ReviewerDecision)

        decision = structured_llm.invoke(messages)

        state["review"] = Review(
            approved=decision.approved,
            feedback=decision.feedback,
            score=decision.score,
        )

        state["current_agent"] = AgentType.REVIEWER

        return state
