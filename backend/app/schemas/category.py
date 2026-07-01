from pydantic import BaseModel
from datetime import datetime

class CategoryCreate(BaseModel):
    name: str
    
class CategoryResponse(BaseModel):
    id: int 
    name: str
    created_at: datetime

class CategoryUpdate(BaseModel):
    id: int
    name: str
    


