import pandas as pd
from fastapi import FastAPI
from routes import sheets

app = FastAPI()

app.include_router(sheets.router)

@app.get("/")
async def root():
  return { "message": "Online" }

