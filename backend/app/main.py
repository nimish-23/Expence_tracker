from fastapi import FastAPI
import os
from app.routes.auth import auth_router

app = FastAPI(title="Expence Tracker", description="A simple expence tracker app", version="1.0.0")

@app.get("/")
def start():
    return {"message": "successfully started the server"}

app.include_router(auth_router)