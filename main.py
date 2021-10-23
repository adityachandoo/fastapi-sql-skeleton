import uvicorn
from fastapi import FastAPI
from api.v1.api import api_router

from db.session import Base, engine

app = FastAPI()

@app.on_event("startup")
def on_starup():
    Base.metadata.create_all(bind=engine)

app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000, log_level="info")
    #uvicorn.run(app, uds="/run/app.sock")
