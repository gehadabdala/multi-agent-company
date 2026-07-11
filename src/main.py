from agents.developer.agent import DeveloperAgent
from shared.enums import AgentType
from shared.models import (
    Task,
    Plan,
    Step,
    CodeArtifact,
    Review,
)

state = {
    "task": Task(request="Build a REST API for an e-commerce website"),
    "plan": Plan(),
    "code": CodeArtifact(),
    "review": Review(),
    "current_agent": AgentType.SUPERVISOR,
    "next_agent": AgentType.SUPERVISOR,
    "messages": [],
}


state["plan"] = Plan(
    steps=[
        Step(description="Create FastAPI project"),
        Step(description="Create Product model"),
        Step(description="Implement CRUD APIs"),
        Step(description="Write unit tests"),
    ]
)

developer = DeveloperAgent()

result = developer.invoke(state)

print(result["code"].content)
