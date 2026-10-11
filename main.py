from fastapi import FastAPI
from fastapi.params import Body
app = FastAPI()


@app.get("/")
def home():
    return "Welcome to to FastAPI using UV"

@app.post("/createPost")
def create_post(payload : dict = Body(...)):
    return {"Data" : payload, "msg" : "Created"}