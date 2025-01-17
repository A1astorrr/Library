from app.books.crud import BookDAO
import pytest

@pytest.mark.parametrize("title, annotation, genre, publisher,author_id", [
    ("Ведьмак", "геральт",  "Фэнтези", "АСТ", 1)
    ])
async def test_add_and_get_books(title, annotation, genre, publisher,author_id):
    new_books = await BookDAO.add(title=title,
    annotation=annotation,
    genre=genre,
    publisher=publisher,
    author_id=author_id)
    
    assert new_books.author_id == 1
    
    new_books = await BookDAO.find_id(new_books.id)
    
    assert new_books is not None