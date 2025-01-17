import pytest
from httpx import AsyncClient

@pytest.mark.parametrize("email,password,role,status_code", [
    ("kot@pes.com", "kotopes", "user", 200),
    ("kot@pes.com", "kot0pes", "user", 409),
    ("pes@kot.com", "pesokot", "user", 200),
    ("abcde", "pesokot", "user", 422),
])
async def test_register_user(email, password, role, status_code, ac: AsyncClient):
    response = await ac.post("auth/register", json={
        "email": email,
        "password": password,
        "role": role,
    })
    
    assert response.status_code == status_code


@pytest.mark.parametrize("email,password,status_code", [
    ("oleg@mail.ru", "oleg", 200),
    ("maks@mail.ru", "maks", 200),
    ("test@test.com", "test", 401),
])
async def test_login_user(email, password,  status_code, ac: AsyncClient):
    response = await ac.post("auth/login", json={
        "email": email,
        "password": password,
    })

        
    assert response.status_code == status_code