from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def index():
    return {"data": "Hello CJ-API!"}


@app.get("/message")
def index():
    return {"data": "CJ-API is great!"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
