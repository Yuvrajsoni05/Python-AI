from dotenv import load_dotenv
from langchain_classic.chains.question_answering.map_reduce_prompt import messages
from typing_extensions import TypedDict
from typing import Optional,Literal
from langgraph.graph import StateGraph
from langgraph.graph import StateGraph,START,END
from openai import  OpenAI


load_dotenv()

client = OpenAI()
class State(TypedDict):
    user_query: str
    llm_output: Optional[str]
    is_good:bool


def chatbot(state:State):
    print(state)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role":"user","content":state["user_query"]},
        ]
    )
    state["llm_output"] =  response.choices[0].message.content
    return state


def evaluate_response(state:State) -> Literal["chatbot_geminin","endnode"]:
    if True:
        return "endnode"
    return "chatbot_gemini"


def chatbot_geminin(state:State):
    print(state)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": state["user_query"]},
        ]
    )
    state["llm_output"] = response.choices[0].message.content
    return state


def endnode(state:State):
    return state

graph_builder = StateGraph(State)
graph_builder.add_node("chatbot",chatbot)
graph_builder.add_node("chatbot_geminin",chatbot_geminin)
graph_builder.add_node("endnode",endnode)

graph_builder.add_edge(START, "chatbot")
graph_builder.add_conditional_edges("chatbot", evaluate_response)

graph_builder.add_edge("chatbot_geminin", "endnode")
graph_builder.add_edge("endnode", END)

graph =  graph_builder.compile()

update_state = graph.invoke(State({"user_query":"Hey what is 2 + 2 ?"}))
print(update_state)

