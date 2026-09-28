from dotenv import load_dotenv
import os

from langgraph.constants import START, END
from langgraph.graph import StateGraph
from typing_extensions import TypedDict
from langchain.chat_models import init_chat_model
load_dotenv()

print(os.getenv("OPENAI_API_KEY"))
model = init_chat_model(
    "openai:gpt-4o-mini",

)
class State(TypedDict):
    message: str



def chatbot(state: State):
    print("We are inside chatbot" , state)
    response = model.invoke(state["message"])
    return {
        "message": response.content
    }




#Create Graph
graph_builder = StateGraph(State)

graph_builder.add_node("chat_bot",chatbot)

graph_builder.add_edge(START, "chat_bot")
graph_builder.add_edge("chat_bot", END)

# 6. Compile Graph
graph = graph_builder.compile()


result = graph.invoke({
    "message": "Hi Yuvraj"
})


print("Final State:", result)