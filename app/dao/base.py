from typing import Generic, TypeVar
from app.database import async_session, Base
from sqlalchemy import delete, select, insert
from typing import Sequence


T = TypeVar("T", bound=Base)

class BaseDAO(Generic[T]):
    model: type[T]

    @classmethod
    async def get_id(cls, id: int) -> T | None:
        async with async_session() as session:
            query = select(cls.model).filter_by(id=id)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def get_all(cls, **filter_by) -> Sequence[T]:
        async with async_session() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def find_one_or_none(cls, **filter_by) -> T | None:
        async with async_session() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def add(cls, **data) -> T:
        async with async_session() as session:
            added = cls.model(**data)
            session.add(added)
            await session.commit()
            await session.refresh(added)
            return added


    @classmethod
    async def delete(cls, **filter_by)  -> T | None:
        async with async_session() as session:
            deleted = await cls.find_one_or_none(**filter_by)
            if deleted is None:
                return None
            query = delete(cls.model).filter_by(**filter_by)
            await session.execute(query)
            await session.commit()
            return deleted
