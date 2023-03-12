from fastapi import APIRouter
from fastapi import Path
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List

from config.database import Session
from services.critic import CriticService
from schemas.critic import Critic

critic_route = APIRouter()


@critic_route.get('/critics', tags=['critic'], response_model=List[Critic], status_code=200)
def get_critics() -> List[Critic]:
    db = Session()
    result = CriticService(db).getCritics()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@critic_route.get('/critic/{id}', tags=['critic'], response_model=Critic, status_code=200)
def get_critic(id: int = Path(ge=1)) -> Critic:
    db = Session()
    result = CriticService(db).getCritic(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Not Found"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@critic_route.post('/critic', tags=['critic'], response_model=dict, status_code=201)
def create_critic(critic: Critic) -> dict:
    db = Session()
    CriticService(db).createCritic(critic)
    return JSONResponse(status_code=201, content={"message": "Critic Created"})


@critic_route.patch('/critic/{id}', tags=['critic'], response_model=dict, status_code=200)
def update_critic(id: int, critic: Critic) -> dict:
    db = Session()
    result = CriticService(db).getCritic(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Not Found"})
    CriticService(db).updateCritic(id, critic)
    return JSONResponse(status_code=200, content={"message": "Critic Updated"})


@critic_route.delete('/critic/{id}', tags=['critic'], response_model=dict, status_code=200)
def delete_critic(id: int) -> dict:
    db = Session()
    result = CriticService(db).getCritic(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Not Found"})
    CriticService(db).deleteCritic(id)
    return JSONResponse(status_code=200, content={"message": "Deleted"})
