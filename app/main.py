from cgi import test
import imp
import fastapi
import psycopg2
from fastapi import FastAPI, Response, status, HTTPException, APIRouter
from fastapi.params import Body, Depends
from sqlalchemy import delete
from sqlalchemy.orm import Session, query
from .database import engine, get_db, Base
from . import models, schema
from psycopg2.extras import RealDictCursor
import time
from .routers import test, game4
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(test.router)
app.include_router(game4.router)

models.Base.metadata.create_all(bind=engine)

# @app.get("/test")
# def player_level_status():
#     curser.execute("""SELECT * FROM player_level""")
#     status1 = curser.fetchall()
#     return status1

# making connection with a database
while True:
    try:
        conn = mysql.connector.connect(host='localhost', database='test_db', user='test_user', password='April2022!')
        curser = conn.cursor()
        print("Database Connection was successfull")
        break
    except Exception as error:
        print("Connection failed")
        print("Error:", error)
        time.sleep(5)