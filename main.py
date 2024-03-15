import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from endpoints.inventory import get_inventory

app = FastAPI()

origins = ["http://localhost:8000",]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def smile():
    return {";-;"}

@app.get("/inventory/{user_id}")
def inventory(user_id: int):
    return {"inventory": get_inventory(user_id)}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
