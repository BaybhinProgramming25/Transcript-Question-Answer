from dotenv import load_dotenv
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker, DeclarativeBase 

load_dotenv(interpolate=True, override=True)
import os 

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL, pool_pre_ping=True, pool_recycle=3600)
SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass 

def get_db():
    db = SessionLocal()
    try:
        yield db 
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


