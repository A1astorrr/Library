from pydantic import BaseModel, ConfigDict
from app.authors.schemas import AuthorBase

class BookBase(BaseModel):
    title: str
    annotation: str
    genre: str
    publisher: str
    author_id: int
    
class BookCreate(BookBase):
    pass

class BookUpdate(BookCreate):
    pass
    
    
class Book(BookBase):
    model_config  = ConfigDict(from_attributes=True)
    author: AuthorBase