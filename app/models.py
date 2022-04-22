import email
from enum import unique
from time import time
from psycopg2 import Time
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from email.policy import default
from pydantic import ColorError
from .database import Base
from sqlalchemy import TIMESTAMP, VARBINARY, VARCHAR, Column, Integer, String, Boolean, TIME

# level information
class Level_master(Base):
    __tablename__ = "tbl_g4_level_master"
    game_id = Column(Integer, nullable=False)
    level_id = Column(Integer, primary_key=True, nullable=False)
    level_name = Column(VARCHAR(50), nullable=False)
    level_word_count = Column(Integer, nullable=False)
    updated_date = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('CURRENT_TIMESTAMP()'))
    level_time = Column(Integer, nullable=False)
    status = Column(Boolean, nullable=False, server_default=text("True"))

# level instructions
class Instructions(Base):
    __tablename__ = "tbl_g4_instruction"
    id = Column(Integer, primary_key=True, nullable=False)
    game_id = Column(Integer, nullable=False)
    level_id = Column(Integer, nullable=False)
    instructions = Column(VARCHAR(50), nullable=False)
    updated_date = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('CURRENT_TIMESTAMP()'))
    status = Column(Boolean, nullable=False, server_default=text("True"))

# user progress
class User_status(Base):
    __tablename__ = "tbl_g4_user_status"
    id = Column(Integer, primary_key=True, nullable=False)
    game_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)
    level_id = Column(Integer, nullable=False)
    status = Column(Boolean, nullable=False, server_default=text("True"))
    updated_date = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('CURRENT_TIMESTAMP()'))
    selected_word = Column(VARCHAR(50), nullable=False)
    points = Column(Integer, nullable=False, server_default='0')
    no_of_words = Column(Integer, nullable=False)

# words posted by user
class Created_words(Base):
    __tablename__ = "tbl_g4_created_words"
    id = Column(Integer, primary_key=True, nullable=False)
    game_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)
    level_id = Column(Integer, nullable=False)
    words = Column(VARCHAR(50), nullable=False)

# level words
class Word_master(Base):
    __tablename__ = "tbl_g4_word_master"
    id = Column(Integer, primary_key=True, nullable=False)
    game_id = Column(Integer, nullable=False)
    level_id = Column(Integer, nullable=False)
    words = Column(VARCHAR(50), nullable=False)

# images of individual levels
class Image_master(Base):
    __tablename__ = "tbl_g4_image_master"
    id = Column(Integer, primary_key=True, nullable=False)
    game_id = Column(Integer, nullable=False)
    level_id = Column(Integer, nullable=False)
    image_url = Column(VARCHAR(100), nullable=False)

# user level

class User_level(Base):
    __tablename__ = "tbl_g4_user_level"
    game_id = Column(Integer, nullable=False)
    user_id = Column(Integer, primary_key=True, nullable=False)
    level_id = Column(Integer, nullable=False)