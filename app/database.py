from sqlalchemy import NullPool
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from  app.config import settings

if settings.MODE == "TEST":
    database_url = settings.test_database_url
    database_params = {"poolclass": NullPool}
else:
    database_url = settings.database_url
    database_params =  {}
    
engine = create_async_engine(
    database_url,
    echo=False,
    **database_params,
)

async_session = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=True)

class Base(DeclarativeBase):
    pass