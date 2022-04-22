import imp
from re import A
from anyio import run_async_from_thread
from fastapi import FastAPI, Response, status, HTTPException, APIRouter
from .. import database, models, main
from fastapi import FastAPI, Response, status, HTTPException, APIRouter
from sqlalchemy.orm import Session, query
from fastapi.params import Body, Depends
from typing import Optional, List
from ..database import get_db
from typing import Optional
from  sqlalchemy.sql.expression import func, select


router = APIRouter()

# @router.get("/player/{id}")
# def player_level_status(id: int):
#     main.curser.execute("""SELECT level_id, status FROM player_level WHERE user_id = %s""", [id])
#     status2 = main.curser.fetchall()
#     return status2


@router.get("/player/{id}")
def player_status(id: int, db: Session = Depends(get_db)):
    player_level = db.query(models.User_level.level_id).filter(models.User_level.user_id == id).first()

    if not player_level:
        levelno = 1
        player_level = {"level_id": levelno}
    return player_level

@router.get("/instruction/{id}")
def level_instruction(id: int, db: Session = Depends(get_db)):
    inst = db.query(models.Instructions.instructions).filter(models.Instructions.level_id == id).all()

    if not inst:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"level with ID: {id} not found")
    return inst

# get words for specific level
@router.get("/words/{id}")
def Instruction(id: int, db: Session = Depends(get_db)):
    words = db.query(models.Word_master.words).filter(models.Word_master.level_id == id).order_by(func.random()).limit(4).all()
    return words

