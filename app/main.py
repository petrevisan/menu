import pandas as pd
from fastapi import FastAPI
from routes.spreadsheets import get_spreadsheet_data
from routes.users import create_user

app = FastAPI()

app.include_router(get_spreadsheet_data.router)
app.include_router(create_user.router)

@app.get("/")
async def root():
  return { "message": "Online" }

