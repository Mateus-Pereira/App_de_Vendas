from fastapi import FastAPI, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from sqlalchemy.orm import Session
from src.schemas.schemas import Produto, Usuario,ProdutoSimples
from src.infra.sql.config.database import get_db, criar_bd
from src.infra.sql.repositorios.produto import RepositorioProduto
from src.infra.sql.repositorios.repositorio_usuario import RepositorioUsuario

# criar_bd()

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
@app.post('/produtos', status_code=status.HTTP_201_CREATED,response_model=Produto)
def criar_produto(produto: Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado

@app.delete('/produtos/{id}')
def remover_produto(id: int, db: Session = Depends(get_db)):
    RepositorioProduto(db).remover(id)
    return

@app.get('/produtos', response_model=List[Produto])
def lista_produto(db: Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar()
    return produtos

@app.put('/produtos/{id}', response_model=ProdutoSimples)
def editar_produto(id: int, produto: Produto, db: Session = Depends(get_db)):
    RepositorioProduto(db).editar(id, produto)
    produto.id = id
    return produto

#Usuarios

@app.post('/signup', status_code=status.HTTP_201_CREATED, response_model=Usuario)
def criar_usuario(usuario: Usuario, session: Session = Depends(get_db)):
    usuario_criado = RepositorioUsuario(session).criar(usuario)
    return usuario_criado

@app.get('/usuarios', response_model=List[Usuario])
def lista_usuario(session: Session = Depends(get_db)):
    usuario = RepositorioUsuario(session).listar()
    return usuario
