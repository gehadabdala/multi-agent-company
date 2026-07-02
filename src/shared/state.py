from typing import Annotated

from typing_extensions import TypedDict

from langgraph.graph.message import add_messages

from langchain_core.messages import BaseMessage

from shared.models import (
    Task,
    Plan,
    CodeArtifact,
    Review,
)
from shared.enums import AgentType


class AgentState(TypedDict):
    """
    Shared state exchanged between all agents.
    """

    task: Task

    plan: Plan

    code: CodeArtifact

    review: Review

    current_agent: AgentType

    next_agent: AgentType

    messages: Annotated[
        list[BaseMessage],
        add_messages,
    ]
