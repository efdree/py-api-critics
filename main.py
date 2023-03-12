from fastapi import FastAPI
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from fastapi.middleware.cors import CORSMiddleware

from routers.user import user_router
from routers.platform import platform_route
from routers.involvedcompany import involvedcompany_route
from routers.critic import critic_route
from routers.genre import genre_route
from routers.gameplatform import gameplatform_route
from routers.gamegenre import gamegenre_route
from routers.game import game_route
from routers.company import company_route

app = FastAPI()
app.title = "Critics API"
app.version = "0.0.1"

origins = [
    "http://localhost:3000",
    "http://localhost:8000",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:8000",
]

app.add_middleware(ErrorHandler)
app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"],
                   )

app.include_router(user_router)
app.include_router(platform_route)
app.include_router(involvedcompany_route)
app.include_router(critic_route)
app.include_router(genre_route)
app.include_router(gameplatform_route)
app.include_router(gamegenre_route)
app.include_router(game_route)
app.include_router(company_route)

Base.metadata.create_all(bind=engine)
