from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from core.db import create_tables
from models.event import Event
from models.user import User

@asynccontextmanager
async def lifespan(app:FastAPI):
    print('app start up ')
    await create_tables()
    yield
    print('app shut down ')


app=FastAPI(title='How Long Ago',lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get("/")
def root():
    return {"message": "Welcome to How Long Ago API!"}