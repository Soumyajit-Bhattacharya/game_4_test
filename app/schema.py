import email
from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime


class player(BaseModel):
    id: int
    user_id: int
    level_id: int
    status: str
    created_at: datetime