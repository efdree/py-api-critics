from fastapi import APIRouter
from fastapi import Path
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List

from config.database import Session
from services.involvedcompany import InvolvedCompanyService
from schemas.involvedcompany import InvolvedCompany

involvedcompany_route = APIRouter()


@involvedcompany_route.get('/involvedcompanies', tags=['involvedcompany'], response_model=List[InvolvedCompany], status_code=200)
def get_involvedcompanies() -> List[InvolvedCompany]:
    db = Session()
    result = InvolvedCompanyService(db).getInvolvedCompanies()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


# @involvedcompany_route.get('/involvedcompany/{id}', tags=['involvedcompany'], response_model=InvolvedCompany, status_code=200)
# def get_platform(id: int = Path(ge=1)) -> InvolvedCompany:
#     db = Session()
#     result = InvolvedCompanyService(db).getInvolvedCompany(id)
#     if not result:
#         return JSONResponse(status_code=404, content={"message": "Not Found"})
#     return JSONResponse(status_code=200, content=jsonable_encoder(result))


@involvedcompany_route.post('/involvedcompany', tags=['involvedcompany'], response_model=dict, status_code=201)
def create_involvedcompany(involvedcompany: InvolvedCompany) -> dict:
    db = Session()
    InvolvedCompanyService(db).createInvolvedCompany(involvedcompany)
    return JSONResponse(status_code=201, content={"message": "InvolvedCompany Created"})


# @involvedcompany_route.patch('/involvedcompany/{id}', tags=['involvedcompany'], response_model=dict, status_code=200)
# def update_involvedcompany(id: int, involvedcompany: InvolvedCompany) -> dict:
#     db = Session()
#     result = InvolvedCompanyService(db).getInvolvedCompany(id)
#     if not result:
#         return JSONResponse(status_code=404, content={"message": "Not Found"})
#     InvolvedCompanyService(db).updateInvolvedCompany(id, involvedcompany)
#     return JSONResponse(status_code=200, content={"message": "InvolvedCompany Updated"})


# @involvedcompany_route.delete('/involvedcompany/{id}', tags=['involvedcompany'], response_model=dict, status_code=200)
# def delete_involvedcompany(id: int) -> dict:
#     db = Session()
#     result = InvolvedCompanyService(db).getInvolvedCompany(id)
#     if not result:
#         return JSONResponse(status_code=404, content={"message": "Not Found"})
#     InvolvedCompanyService(db).deleteInvolvedCompany(id)
#     return JSONResponse(status_code=200, content={"message": "Deleted"})
