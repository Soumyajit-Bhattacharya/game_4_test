import imp
from itertools import count
from fastapi import FastAPI, Response, status, HTTPException, APIRouter
from .. import database, models, main
from fastapi import FastAPI, Response, status, HTTPException, APIRouter
from sqlalchemy.orm import Session, query
from fastapi.params import Body, Depends
from typing import Dict, Optional, List
from ..database import get_db
from typing import Optional
import mysql.connector
from pydantic import BaseModel

router = APIRouter(
    tags=['player status']
)

class POST(BaseModel):
    words: list

@router.post("/test", response_model=POST)
def player_level_status(words: POST, db: Session = Depends(get_db)):
    a = words.words[1]
    print(a)
    return words


