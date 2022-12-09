import port as port
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def index():
    return {"massage": "hello_world"}


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
