from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
from fastapi import HTTPException, Request

import os, jwt

load_dotenv()

ALGORITHM = "HS256"
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

def get_current_user(request: Request):

    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    payload = verify_token(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid or Expired JWT token. Please log in again.")
    return payload


def create_token(data: dict) -> str:

    global JWT_SECRET_KEY, ALGORITHM
    
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(hours=1) 
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=ALGORITHM)
    return token 

def verify_token(token: str):

    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
        return None # Invalid JWT token provided