import datetime
from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class Author(Base):
    __tablename__ = "authors"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(index=True)
    surname: Mapped[str] = mapped_column(index=True)
    date_birth: Mapped[datetime.datetime]
    biography: Mapped[str]