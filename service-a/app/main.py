import uvicorn
import requests
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    rfield: str = "123"
    ofield: Optional[str] = "456"

app = FastAPI(title="Service-A")


@app.get("/testa")
def checka():
    # for demo purpose. Create a question from that.
    options = [
        "http://localhost/service-b/testb",
        "http://localhost:8001/service-b/testb",
        "http://localhost:8000/service-b/testb",
        "http://service-b/testb",
        "http://service-b:8000/testb",
        "http://service-b:8001/testb"
        "http://0.0.0.0/service-b/testb",
        "http://0.0.0.0:8001/service-b/testb",
        "http://0.0.0.0:8000/service-b/testb",
        "http://127.0.0.1/service-b/testb",
        "http://127.0.0.1:8001/service-b/testb",
        "http://127.0.0.1:8000/service-b/testb",
        "http://host.docker.internal:8000/service-b/testb",
        "http://host.docker.internal:8001/service-b/testb",
        "http://testnet:8000/service-b/testb",
        "http://testnet:8001/service-b/testb",
    ]
    for path in options:
        try:
            resp = requests.get(path)
        except:
            print("ERROR:","."*10,path,"."*10)
            continue
        else:
            print("SUCCESS:","-"*10,path,"-"*10)
            print(resp.text)
    print("~"*20)
    return {"response": "END"}


@app.post("/test-body")
def check_body(request: Item):
    return request


@app.get("/test-body/get")
def check_body_get(request: Item):
    return request


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")