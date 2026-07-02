from graph.builder import graph
from shared.models import Task, Plan, CodeArtifact, Review
from shared.enums import AgentType


def test_supervisor_routes_to_planner():

    state = {
        "task": Task(request="Build FastAPI CRUD API"),
        "plan": Plan(),
        "code": CodeArtifact(),
        "review": Review(),
        "current_agent": AgentType.SUPERVISOR,
        "next_agent": AgentType.SUPERVISOR,
        "messages": [],
    }

    result = graph.invoke(state)

    assert result["next_agent"] == AgentType.PLANNER
