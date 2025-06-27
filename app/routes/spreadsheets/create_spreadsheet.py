from fastapi import APIRouter
from pydantic import BaseModel

class CreateSpreadsheet(BaseModel):
  url: str

router = APIRouter()

@router.post("/spreadsheets", tags=["planilhas"])
async def create_spreadsheet_data(url: CreateSpreadsheet) -> dict:
  return { "message": "It worked so fucking well"}