from langgraph.graph import StateGraph, START, END

from shared.state import AgentState
from agents.supervisor.agent import SupervisorAgent

supervisor = SupervisorAgent()

builder = StateGraph(AgentState)

builder.add_node(
    "supervisor",
    supervisor.invoke,
)

builder.add_edge(
    START,
    "supervisor",
)

builder.add_edge(
    "supervisor",
    END,
)

graph = builder.compile()
