from pydantic import BaseModel, ConfigDict, field_validator
from app.authors.schemas import AuthorBase


class BookBase(BaseModel):
    title: str | None = None
    annotation: str | None = None
    genre: str | None = None
    publisher: str | None = None
    author_id: int
    
    @field_validator("title", "annotation","genre", "publisher", mode="before")
    def set_empty_string(cls, v):
        return v or ""
    
class BookCreate(BookBase):
    image_id: int | None = None
    

class BookUpdate(BookCreate):
    pass
    
    
class Book(BookBase):
    model_config  = ConfigDict(from_attributes=True)
    author: AuthorBase