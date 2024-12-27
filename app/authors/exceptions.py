from fastapi import HTTPException, status

AuthorByIdNotFoundException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Автор не найден"
)

AuthorNotCreatedException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Ошибка в создание автора",
)

AuthorNotUpdateException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Автор не обновлен",
)

NotDeletedByIdException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Автор не найден"
)

