from dotenv import load_dotenv

load_dotenv()
from fastapi import FastAPI, Query
from queues.worker import process_query
from client.rq_client import queue


app = FastAPI()


@app.get("/")
def root():
    return {"Hello": "World"}
# {
#   "status": "queued",
#   "job_id": "ddf5bba2-283b-422b-841c-db5ea71935fe"
# }

@app.post("/chat")
def chat(
    query: str = Query(..., description="The chat query of user"),
):
    job = queue.enqueue(process_query,query)
    print(job)
    return {"status" : "queued","job_id": job.id}


@app.get("/job-status")
def get_result(job_id:str=Query(...,description="Job ID")):
    job = queue.fetch_job(job_id)
    result = job.return_value()
    return {"result": result}


