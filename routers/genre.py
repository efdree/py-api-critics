from fastapi import APIRouter
from fastapi import Path
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List

from config.database import Session
from services.genre import GenreService
from schemas.genre import Genre

genre_route = APIRouter()


@genre_route.get('/genres', tags=['genre'], response_model=List[Genre], status_code=200)
def get_genres() -> List[Genre]:
    db = Session()
    result = GenreService(db).getGenres()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


# @genre_route.get('/genre/{id}', tags=['genre'], response_model=Genre, status_code=200)
# def get_genre(id: int = Path(ge=1)) -> Genre:
#     db = Session()
#     result = GenreService(db).getGenre(id)
#     if not result:
#         return JSONResponse(status_code=404, content={"message": "Not Found"})
#     return JSONResponse(status_code=200, content=jsonable_encoder(result))


@genre_route.post('/genre', tags=['genre'], response_model=dict, status_code=201)
def create_genre(genre: Genre) -> dict:
    db = Session()
    GenreService(db).createGenre(genre)
    return JSONResponse(status_code=201, content={"message": "Genre Created"})


# @genre_route.patch('/genre/{id}', tags=['genre'], response_model=dict, status_code=200)
# def update_genre(id: int, genre: Genre) -> dict:
#     db = Session()
#     result = GenreService(db).getGenre(id)
#     if not result:
#         return JSONResponse(status_code=404, content={"message": "Not Found"})
#     GenreService(db).updateGenre(id, genre)
#     return JSONResponse(status_code=200, content={"message": "Genre Updated"})


# @genre_route.delete('/genre/{id}', tags=['genre'], response_model=dict, status_code=200)
# def delete_genre(id: int) -> dict:
#     db = Session()
#     result = GenreService(db).getGenre(id)
#     if not result:
#         return JSONResponse(status_code=404, content={"message": "Not Found"})
#     GenreService(db).deleteGenre(id)
#     return JSONResponse(status_code=200, content={"message": "Deleted"})
