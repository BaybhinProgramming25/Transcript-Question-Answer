from fastapi import APIRouter, Depends, HTTPException, Form
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from database.database import get_db
from database.models import Document
from helpers.jwt import get_current_user
from rag import query

import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
router = APIRouter()


@router.post("/parse")
def parse(
    message: str = Form(...),
    document_id: int = Form(...),
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    if not message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty")

    doc = db.query(Document).filter(
        Document.id == document_id,
        Document.user_email == current_user["username"]
    ).first()
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")

    answer = query(message, doc.id, OPENAI_API_KEY)
    return JSONResponse(content={"message": answer})
