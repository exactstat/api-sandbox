import uvicorn
from fastapi import FastAPI

app = FastAPI(title="Service-B")


@app.get("/testb")
def testb():
    return {"response": "Test B"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
