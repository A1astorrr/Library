from pydantic import BaseModel, EmailStr
from enum import Enum

class UserRole(str, Enum):
    admin = "admin"
    user = "user"
    editor = "editor"

class SUserAuth(BaseModel):
    email: EmailStr
    password: str
    
    
class SUserAuthAdmin(SUserAuth):
    role: UserRole = UserRole.user