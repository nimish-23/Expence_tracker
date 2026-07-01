from pydantic import BaseModel
from datetime import datetime

class ExpenseCreate(BaseModel):
    title: str
    amount: float
    description: str
    date: datetime
    category_id: int

class ExpenseResponse(BaseModel):
    id: int
    title: str  
    amount: float
    description: str
    date: datetime


class ExpenseUpdate(BaseModel):
    title: str
    amount: float
    description: str
    date: datetime



