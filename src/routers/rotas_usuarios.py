from fastapi import APIRouter, status, Depends
from typing import List
from sqlalchemy.orm import Session
from src.schemas.schemas import Usuario
from src.infra.sql.config.database import get_db
from src.infra.sql.repositorios.repositorio_usuario import RepositorioUsuario


router = APIRouter()

@router.post('/signup', status_code=status.HTTP_201_CREATED, response_model=Usuario)
def criar_usuario(usuario: Usuario, session: Session = Depends(get_db)):
    usuario_criado = RepositorioUsuario(session).criar(usuario)
    return usuario_criado

@router.get('/usuarios', response_model=List[Usuario])
def lista_usuario(session: Session = Depends(get_db)):
    usuario = RepositorioUsuario(session).listar()
    return usuario
