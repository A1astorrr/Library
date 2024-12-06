from fastapi import HTTPException, status

BookByIdNotFound = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Запись не найдена."
)

AuthorByIdNotFound = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Автор не найден."
)

BookNotCreated = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Ошибка в создание книги.",
)

BookNotUpdate = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Книга не обновлена.",
)

NotDeletedById = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Книга не найдена."
)

