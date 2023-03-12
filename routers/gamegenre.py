from fastapi import APIRouter
from fastapi import Path
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List

from config.database import Session
from services.gamegenre import GameGenreService
from schemas.gamegenre import GameGenre

gamegenre_route = APIRouter()


@gamegenre_route.get('/gamesgenres', tags=['gamegenre'], response_model=List[GameGenre], status_code=200)
def get_gamesgenres() -> List[GameGenre]:
    db = Session()
    result = GameGenreService(db).getGamesGenres()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


# @gamegenre_route.get('/gamegenre/{id}', tags=['gamegenre'], response_model=GameGenre, status_code=200)
# def get_gamegenre(id: int = Path(ge=1)) -> GameGenre:
#     db = Session()
#     result = GameGenreService(db).getGameGenre(id)
#     if not result:
#         return JSONResponse(status_code=404, content={"message": "Not Found"})
#     return JSONResponse(status_code=200, content=jsonable_encoder(result))


@gamegenre_route.post('/gamegenre', tags=['gamegenre'], response_model=dict, status_code=201)
def create_gamegenre(gamegenre: GameGenre) -> dict:
    db = Session()
    GameGenreService(db).createGameGenre(gamegenre)
    return JSONResponse(status_code=201, content={"message": "GameGenre Created"})


# @gamegenre_route.patch('/gamegenre/{id}', tags=['gamegenre'], response_model=dict, status_code=200)
# def update_gamegenre(id: int, gamegenre: GameGenre) -> dict:
#     db = Session()
#     result = GameGenreService(db).getGameGenre(id)
#     if not result:
#         return JSONResponse(status_code=404, content={"message": "Not Found"})
#     GameGenreService(db).updateGameGenre(id, gamegenre)
#     return JSONResponse(status_code=200, content={"message": "GameGenre Updated"})


# @gamegenre_route.delete('/gamegenre/{id}', tags=['gamegenre'], response_model=dict, status_code=200)
# def delete_gamegenre(id: int) -> dict:
#     db = Session()
#     result = GameGenreService(db).getGameGenre(id)
#     if not result:
#         return JSONResponse(status_code=404, content={"message": "Not Found"})
#     GameGenreService(db).deleteGameGenre(id)
#     return JSONResponse(status_code=200, content={"message": "Deleted"})
