from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from  app.config import settings

engine = create_async_engine(
    url=settings.Database_url,
    echo=False,
)

async_session = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=True)

class Base(DeclarativeBase):
    pass