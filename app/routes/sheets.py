from fastapi import APIRouter
from pydantic import BaseModel
from services.spreadsheet_reader import spreadsheet_reader

class SheetsReader(BaseModel):
  url: str

router = APIRouter()

@router.post("/sheets")
async def get_sheets_url(url: SheetsReader) -> dict:
  result = spreadsheet_reader(url.url)
  return { "message": result }