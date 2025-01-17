import pytest
from httpx import AsyncClient


@pytest.mark.parametrize("title, annotation, genre, publisher,author_id, status_code", [
    ("Ведьмак", "геральт",  "Фэнтези", "АСТ", 1, 200),
    ("Ведьмак", "геральт",  "Фэнтези", "АСТ", 3, 404)
    ])
async def test_add_and_get_books(title, annotation, genre, publisher,author_id,status_code,authenticated_ac: AsyncClient):
    response = await authenticated_ac.post("/books/", params={
        "title":title,
        "annotation":annotation,
        "genre":genre,
        "publisher":publisher,
        "author_id":author_id
    })
    
    assert response.status_code == status_code
    
    