from fastapi import APIRouter
from fastapi import Path
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List

from config.database import Session
from services.gameplatform import GamePlatformService
from schemas.gameplatform import GamePlatform

gameplatform_route = APIRouter()


@gameplatform_route.get('/gamesplatforms', tags=['gameplatform'], response_model=List[GamePlatform], status_code=200)
def get_gameplatform() -> List[GamePlatform]:
    db = Session()
    result = GamePlatformService(db).getGamePlatforms()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


# @gameplatform_route.get('/gameplatform/{id}', tags=['gameplatform'], response_model=GamePlatform, status_code=200)
# def get_gameplatform(id: int = Path(ge=1)) -> GamePlatform:
#     db = Session()
#     result = GamePlatformService(db).getGamePlatform(id)
#     if not result:
#         return JSONResponse(status_code=404, content={"message": "Not Found"})
#     return JSONResponse(status_code=200, content=jsonable_encoder(result))


@gameplatform_route.post('/gameplatform', tags=['gameplatform'], response_model=dict, status_code=201)
def create_gameplatform(gameplatform: GamePlatform) -> dict:
    db = Session()
    GamePlatformService(db).createGamePlatform(gameplatform)
    return JSONResponse(status_code=201, content={"message": "GamePlatform Created"})


# @gameplatform_route.patch('/gameplatform/{id}', tags=['gameplatform'], response_model=dict, status_code=200)
# def update_gameplatform(id: int, gameplatform: GamePlatform) -> dict:
#     db = Session()
#     result = GamePlatformService(db).getGamePlatform(id)
#     if not result:
#         return JSONResponse(status_code=404, content={"message": "Not Found"})
#     GamePlatformService(db).updateGamePlatform(id, gameplatform)
#     return JSONResponse(status_code=200, content={"message": "GamePlatform Updated"})


# @gameplatform_route.delete('/gameplatform/{id}', tags=['gameplatform'], response_model=dict, status_code=200)
# def delete_gameplatform(id: int) -> dict:
#     db = Session()
#     result = GamePlatformService(db).getGamePlatform(id)
#     if not result:
#         return JSONResponse(status_code=404, content={"message": "Not Found"})
#     GamePlatformService(db).deleteGamePlatform(id)
#     return JSONResponse(status_code=200, content={"message": "Deleted"})
