from sqladmin import ModelView
from app.authors.models import Author
from app.books.models import Book
from app.users.models import User

class UsersAdmin(ModelView, model=User):
    column_list = [User.id, User.email]
    column_details_exclude_list =  [User.hashed_password]
    can_delete=False
    name = "Пользователь"
    name_plural = "Пользователи"
    icon = "fa-solid fa-user"
    category = "Аккаунты"
    

class BooksAdmin(ModelView, model=Book):
    column_list = [c.name for c in Book.__table__.c] + [Book.author]
    name = "Книга"
    name_plural = "Книги"
    icon = "fa-solid fa-book"
    category = "Книжки"
    
class AuthorsAdmin(ModelView, model=Author):
    column_list = [c.name for c in Author.__table__.c] + [Author.books]
    name = "Автор"
    name_plural = "Авторы"
    icon = "fa-solid fa-user-pen"
    category = "Авторы"