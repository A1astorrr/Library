from pydantic import BaseModel, ConfigDict
from datetime import date

class AuthorBase(BaseModel):
    name: str
    surname: str
    date_birth: date
    biography: str

class AuthorCreate(AuthorBase):
    pass

class AuthorUpdate(AuthorCreate):
    pass
    
    
class Author(AuthorBase):
    model_config  = ConfigDict(from_attributes=True)
    id: int
    
    