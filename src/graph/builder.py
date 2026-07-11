from langgraph.graph import StateGraph, START, END

from agents.planner.agent import PlannerAgent
from shared.enums import AgentType
from shared.state import AgentState
from agents.supervisor.agent import SupervisorAgent

supervisor = SupervisorAgent()
planner = PlannerAgent()
builder = StateGraph(AgentState)

builder.add_node(
    "supervisor",
    supervisor.invoke,
)
builder.add_node(
    "planner",
    planner.invoke,
)


def supervisor_router(state: AgentState):

    if state["next_agent"] == AgentType.PLANNER:
        return "planner"

    return END


builder.add_edge(
    START,
    "supervisor",
)

builder.add_conditional_edges(
    "supervisor",
    supervisor_router,
)

builder.add_edge(
    "planner",
    END,
)

graph = builder.compile()
