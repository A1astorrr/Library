import json
import pytest
import asyncio
from sqlalchemy import insert
from app.database import Base, async_session, engine
from app.config import settings
from app.books.models import Book
from app.authors.models import Author
from app.users.models import User

from datetime import datetime
from httpx import AsyncClient, ASGITransport
from app.main import app as fastapi_app


@pytest.fixture(scope="session", autouse=True)
async def prepare_database():
    assert settings.MODE == "TEST"
    
    # Создание и очистка базы данных
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    
    # Функция для открытия JSON-файлов с данными
    def open_mock_json(model: str):
        with open(f"app/tests/mock_{model}.json", encoding="utf-8") as file:
            return json.load(file)
    
    authors = open_mock_json("authors")
    books = open_mock_json("books")
    users = open_mock_json("users")

    # Преобразование даты рождения авторов в формат даты
    for author in authors:
        author["date_birth"] = datetime.strptime(author["date_birth"], "%Y-%m-%d").date()
        
    # Вставка данных в базу
    async with async_session() as session:
        await session.execute(insert(Author).values(authors))
        await session.execute(insert(Book).values(books))
        await session.execute(insert(User).values(users))
        
        await session.commit()
        


@pytest.fixture(scope="function") 
async def ac():
    async with AsyncClient(transport=ASGITransport(app=fastapi_app), base_url="http://test") as ac:
        yield ac

@pytest.fixture(scope="session") 
async def authenticated_ac():
    async with AsyncClient(transport=ASGITransport(app=fastapi_app), base_url="http://test") as ac:
        await ac.post("auth/login", json={
            "email": "oleg@mail.ru",
            "password": "oleg",
        })
        assert ac.cookies["books_access_token"]
        yield ac


