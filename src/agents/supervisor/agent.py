from langchain_core.messages import HumanMessage, SystemMessage

from services.llm import llm
from shared.enums import AgentType
from shared.state import AgentState

from .prompt import SUPERVISOR_SYSTEM_PROMPT


class SupervisorAgent:

    def invoke(self, state: AgentState) -> AgentState:

        request = state["task"].request

        messages = [
            SystemMessage(content=SUPERVISOR_SYSTEM_PROMPT),
            HumanMessage(content=request),
        ]

        response = llm.invoke(messages)

        print(response.content)

        state["current_agent"] = AgentType.SUPERVISOR

        return state
