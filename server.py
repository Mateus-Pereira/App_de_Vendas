from fastapi import FastAPI, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from sqlalchemy.orm import Session
from src.infra.sql.config.database import get_db
from src.routers import rotas_produtos,rotas_usuarios

app = FastAPI()

#CORS
origins = ['http://localhost:8000']

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

#PRODUTOS
app.include_router(rotas_produtos.router)

#Usuarios
app.include_router(rotas_usuarios.router)