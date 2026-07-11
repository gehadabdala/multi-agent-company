from langchain_core.messages import HumanMessage, SystemMessage

from agents.base import BaseAgent
from agents.supervisor.prompt import system_prompt
from agents.supervisor.schema import SupervisorDecision
from services.llm import llm
from shared.enums import AgentType
from shared.state import AgentState
from agents.base import BaseAgent


class SupervisorAgent(BaseAgent):

    def invoke(self, state: AgentState) -> AgentState:

        request = state["task"].request

        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=request),
        ]

        structured_llm = llm.with_structured_output(SupervisorDecision)

        decision = structured_llm.invoke(messages)

        state["current_agent"] = AgentType.SUPERVISOR
        state["next_agent"] = decision.next_agent

        return state
