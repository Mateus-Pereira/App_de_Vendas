from fastapi import APIRouter, status, Depends
from typing import List
from sqlalchemy.orm import Session
from src.schemas.schemas import Produto,ProdutoSimples
from src.infra.sql.config.database import get_db
from src.infra.sql.repositorios.produto import RepositorioProduto

router = APIRouter()

#PRODUTOS
@router.post('/produtos', status_code=status.HTTP_201_CREATED,response_model=Produto)
def criar_produto(produto: Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado

@router.delete('/produtos/{id}')
def remover_produto(id: int, db: Session = Depends(get_db)):
    RepositorioProduto(db).remover(id)
    return

@router.get('/produtos', response_model=List[Produto])
def lista_produto(db: Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar()
    return produtos

@router.put('/produtos/{id}', response_model=ProdutoSimples)
def editar_produto(id: int, produto: Produto, db: Session = Depends(get_db)):
    RepositorioProduto(db).editar(id, produto)
    produto.id = id
    return produto
