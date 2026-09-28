from langgraph.graph import StateGraph,START,END
from langchain.chat_models import init_chat_model
from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages

llm = init_chat_model(
    model="gpt-4.1-mini"
)


class State(TypedDict):
    message: Annotated[list[str], add_messages]


def chatbot(state: State):
    print("\n\n Inside chatbot", state)
    return {"message" : ["Hi there this is message from chatbot"]}

def samplenode(state: State):
    print("\n\n Inside samplenode", state)
    return {"message" : ["Hi there this is message from sample node"]}



graph_builder = StateGraph(State)
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("samplenode", samplenode)

graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", "samplenode")
graph_builder.add_edge("samplenode", END)
graph =  graph_builder.compile()
update_state = graph.invoke(State({"messages":["Hi, My name is Yuvraj Soni"]}))
print("\n\n This is update state ",update_state)
# print(graph_builder)
state =  {"message" : ["Hi there"]}