from fastapi import HTTPException, status

AuthorByIdNotFound = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Author not found."
)

AuthorNotCreated = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Error in creating the author.",
)

AuthorNotUpdate = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="The author has not been updated.",
)

NotDeletedById = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Author not found."
)

