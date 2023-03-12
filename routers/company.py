from fastapi import APIRouter
from fastapi import Path
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List, Dict

from config.database import Session
from services.company import CompanyService
from schemas.company import Company
from services.game import GameService
from schemas.game import Game
from services.critic import CriticService
from schemas.critic import Critic

company_route = APIRouter()


@company_route.get('/companies', tags=['company'], response_model=List[Company], status_code=200)
def get_companies() -> List[Company]:
    db = Session()
    result = CompanyService(db).getCompanies()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@company_route.get('/company/{id}', tags=['company'], response_model=Dict[Company, Critic], status_code=200)
def get_company(id: int = Path(ge=1)) -> Dict[Company, Critic]:
    db = Session()
    result_company = CompanyService(db).getCompany(id)
    if not result_company:
        return JSONResponse(status_code=404, content={"message": "Not Found"})
    result_critics = CriticService(db).getCriticsByCompany(id)
    return JSONResponse(status_code=200, content=jsonable_encoder([result_company, result_critics]))


@company_route.get('/company/{id}/games', tags=['company'], response_model=Dict[Company, Game], status_code=200)
def get_games_of_company(id: int = Path(ge=1)) -> Dict[Company, Game]:
    db = Session()
    result_company = CompanyService(db).getCompany(id)
    if not result_company:
        return JSONResponse(status_code=404, content={"message": "Not Found"})
    result_games = GameService(db).getGamesByCompany(id)
    return JSONResponse(status_code=200, content=jsonable_encoder([result_company, result_games]))


@company_route.post('/company', tags=['company'], response_model=dict, status_code=201)
def create_company(company: Company) -> dict:
    db = Session()
    CompanyService(db).createCompany(company)
    return JSONResponse(status_code=201, content={"message": "Company Created"})


@company_route.patch('/company/{id}', tags=['company'], response_model=dict, status_code=200)
def update_company(id: int, company: Company) -> dict:
    db = Session()
    result = CompanyService(db).getCompany(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Not Found"})
    CompanyService(db).updateCompany(id, company)
    return JSONResponse(status_code=200, content={"message": "Company Updated"})


@company_route.delete('/critic/{id}', tags=['critic'], response_model=dict, status_code=200)
def delete_company(id: int) -> dict:
    db = Session()
    result = CompanyService(db).getCompany(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Not Found"})
    CompanyService(db).deleteCompany(id)
    return JSONResponse(status_code=200, content={"message": "Deleted"})
