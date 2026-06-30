from typing import Annotated

from typing_extensions import TypedDict

from langgraph.graph.message import add_messages

from langchain_core.messages import BaseMessage


class AgentState(TypedDict):

    user_request: str

    current_agent: str

    next_agent: str

    plan: str

    code: str

    review: str

    final_answer: str

    messages: Annotated[
        list[BaseMessage],
        add_messages,
    ]
