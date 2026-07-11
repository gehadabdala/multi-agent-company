from langchain_core.messages import HumanMessage, SystemMessage

from agents.base import BaseAgent
from agents.developer.prompt import system_prompt


from services.llm import llm

from shared.models import CodeArtifact
from shared.state import AgentState
from shared.enums import AgentType


class DeveloperAgent(BaseAgent):

    def invoke(
        self,
        state: AgentState,
    ) -> AgentState:

        plan = "\n".join(f"- {step.description}" for step in state["plan"].steps)

        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=plan),
        ]

        # structured_llm = llm.with_structured_output(DeveloperResponse)

        # response = structured_llm.invoke(messages)
        response = llm.invoke(messages)

        state["code"] = CodeArtifact(
            content=response.content,
            language="python",
        )

        state["current_agent"] = AgentType.DEVELOPER

        return state
