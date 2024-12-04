from pydantic import BaseModel, ConfigDict
from datetime import datetime
from app.authors.schemas import AuthorBase
from typing import Annotated
from fastapi import Depends

class BookBase(BaseModel):
    title: str
    annotation: str
    date_publishing: datetime
    author_id: Annotated[AuthorBase, Depends()]
    
class BookCreate(BookBase):
    pass

class BookUpdate(BookCreate):
    pass
    
    
class Book(BookBase):
    model_config  = ConfigDict(from_attributes=True)
    
    id: int