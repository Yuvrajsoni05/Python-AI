from dotenv import load_dotenv
from langgraph.graph import StateGraph, START, END
from langchain.chat_models import init_chat_model
from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages

load_dotenv()


# Create OpenAI model
llm = init_chat_model(
    model="openai:gpt-4.1-mini"
)


class State(TypedDict):
    messages: Annotated[list[str], add_messages]


# Node 1
def chatbot(state: State):
    print("\nInside chatbot:", state)

    # Send user's message to OpenAI
    response = llm.invoke(state["messages"])

    return {
        "messages": [response]
    }


# Node 2
def samplenode(state: State):
    print("\nInside samplenode:", state)

    return {
        "messages": ["Message from sample node"]
    }


# Create graph
graph_builder = StateGraph(State)

# Add nodes
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("samplenode", samplenode)

# Define flow
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", "samplenode")
graph_builder.add_edge("samplenode", END)

# Compile
graph = graph_builder.compile()


# Run graph
update_state = graph.invoke({
    "messages": ["Hi, My name is Yuvraj Soni"]
})

print("\nFinal State:", update_state)