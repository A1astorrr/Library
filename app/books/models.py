import datetime
from sqlalchemy import func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base
from typing import Annotated

created_at = Annotated[datetime.datetime, mapped_column(server_default=func.now())]

class Book(Base):
    __tablename__ = "books"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(index=True)
    annotation: Mapped[str]
    date_publishing: Mapped[created_at]
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))
    
    