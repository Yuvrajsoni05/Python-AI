from dotenv import load_dotenv
from langgraph.graph import StateGraph, START, END
from langchain.chat_models import init_chat_model
from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.checkpoint.mongodb import MongoDBSaver
load_dotenv()


# Create OpenAI model
llm = init_chat_model(
    model="openai:gpt-4.1-mini"
)


class State(TypedDict):
    messages: Annotated[list[str], add_messages]


# Node 1
def chatbot(state: State):
    # print("\nInside chatbot:", state)

    # Send user's message to OpenAI
    response = llm.invoke(state["messages"])

    return {
        "messages": [response]
    }


# Node 2
def samplenode(state: State):
    # print("\nInside samplenode:", state)

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


def compile_graph_with_checkpoint(checkpointer):
    return graph_builder.compile(checkpointer=checkpointer)


DB_URL = "mongodb://admin:admin@localhost:27017"

with MongoDBSaver.from_conn_string(DB_URL) as checkpointer:

    graph_with_checkpoint = compile_graph_with_checkpoint(
        checkpointer=checkpointer
    )

    config = {
        "configurable": {
            "thread_id": "yuvraj_thread",
        }
    }

    # update_state = graph_with_checkpoint.invoke(
    #     {
    #         "messages": ["what is my name"]
    #     },
    #     config=config
    # )
    for chunk in graph_with_checkpoint.stream(
            State({"messages": ["what is my name"]}),
            config,
            stream_mode="values"):
        chunk["messages"][-1].pretty_print()

    # print("\nFinal State:", update_state)