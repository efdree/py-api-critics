from fastapi import APIRouter
from fastapi import Path
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List, Dict

from config.database import Session
from services.game import GameService
from schemas.game import Game
from services.critic import CriticService
from schemas.critic import Critic

game_route = APIRouter()


@game_route.get('/games', tags=['game'], response_model=List[Game], status_code=200)
def get_games() -> List[Game]:
    db = Session()
    result = GameService(db).getGames()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@game_route.get('/game/{id}', tags=['game'], response_model=Dict[Game, Critic], status_code=200)
def get_game(id: int = Path(ge=1)) -> Game:
    db = Session()
    result_game = GameService(db).getGame(id)
    if not result_game:
        return JSONResponse(status_code=404, content={"message": "Not Found"})
    result_critics = CriticService(db).getCriticsByGame(id)
    return JSONResponse(status_code=200, content=jsonable_encoder([result_game, result_critics]))


@ game_route.post('/game', tags=['game'], response_model=dict, status_code=201)
def create_game(game: Game) -> dict:
    db = Session()
    GameService(db).createGame(game)
    return JSONResponse(status_code=201, content={"message": "Game Created"})


@ game_route.patch('/game/{id}', tags=['game'], response_model=dict, status_code=200)
def update_game(id: int, game: Game) -> dict:
    db = Session()
    result = GameService(db).getGame(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Not Found"})
    GameService(db).updateGame(id, game)
    return JSONResponse(status_code=200, content={"message": "Game Updated"})


@ game_route.delete('/game/{id}', tags=['game'], response_model=dict, status_code=200)
def delete_game(id: int) -> dict:
    db = Session()
    result = GameService(db).getGame(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Not Found"})
    GameService(db).deleteGame(id)
    return JSONResponse(status_code=200, content={"message": "Deleted"})
