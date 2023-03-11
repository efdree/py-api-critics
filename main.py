from fastapi import FastAPI
from config.database import engine, Base
from fastapi.middleware.cors import CORSMiddleware


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

Base.metadata.create_all(bind=engine)
