from fastapi import HTTPException, status

AuthorByIdNotFound = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Автор не найден."
)

AuthorNotCreated = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Ошибка в создание автора.",
)

AuthorNotUpdate = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Автор не обновлен.",
)

NotDeletedById = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Автор не найден."
)

