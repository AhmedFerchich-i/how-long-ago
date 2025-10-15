from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app=FastAPI(title='How Long Ago')

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