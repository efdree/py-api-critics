from fastapi import APIRouter
from fastapi import Path
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List

from config.database import Session
from services.platform import PlatformService
from schemas.platform import Platform

platform_route = APIRouter()


@platform_route.get('/plataforms', tags=['platform'], response_model=List[Platform], status_code=200)
def get_platforms() -> List[Platform]:
    db = Session()
    result = PlatformService(db).getPlatforms()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


# @platform_route.get('/platform/{id}', tags=['platform'], response_model=Platform, status_code=200)
# def get_platform(id: int = Path(ge=1)) -> Platform:
#     db = Session()
#     result = PlatformService(db).getPlatform(id)
#     if not result:
#         return JSONResponse(status_code=404, content={"message": "Not Found"})
#     return JSONResponse(status_code=200, content=jsonable_encoder(result))


@platform_route.post('/platform', tags=['platform'], response_model=dict, status_code=201)
def create_platform(platform: Platform) -> dict:
    db = Session()
    PlatformService(db).createPlatform(platform)
    return JSONResponse(status_code=201, content={"message": "Platform Created"})


# @platform_route.patch('/platform/{id}', tags=['platform'], response_model=dict, status_code=200)
# def update_platform(id: int, platform: Platform) -> dict:
#     db = Session()
#     result = PlatformService(db).getPlatform(id)
#     if not result:
#         return JSONResponse(status_code=404, content={"message": "Not Found"})
#     PlatformService(db).updatePlatform(id, platform)
#     return JSONResponse(status_code=200, content={"message": "Platform Updated"})


# @platform_route.delete('/platform/{id}', tags=['platform'], response_model=dict, status_code=200)
# def delete_platform(id: int) -> dict:
#     db = Session()
#     result = PlatformService(db).getPlatform(id)
#     if not result:
#         return JSONResponse(status_code=404, content={"message": "Not Found"})
#     PlatformService(db).deletePlatform(id)
#     return JSONResponse(status_code=200, content={"message": "Deleted"})
