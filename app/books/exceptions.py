from fastapi import HTTPException, status

BookByIdNotFoundException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Книга не найдена"
)

AuthorByIdNotFoundException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Автор не найден"
)

BookNotCreatedException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Ошибка в создание книги",
)

BookNotUpdateException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Книга не обновлена",
)

NotDeletedByIdException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Книга не найдена"
)

