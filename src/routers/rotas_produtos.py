from fastapi import APIRouter, status, Depends, HTTPException
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

@router.get('/produtos/{id}')
def exibir_produto(id: int, db: Session = Depends(get_db)):
    produto_localizado = RepositorioProduto(db).buscaPorId(id)
    if not produto_localizado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Produto com esse id = {id} não encontrado')
    return produto_localizado

@router.put('/produtos/{id}', response_model=ProdutoSimples)
def editar_produto(id: int, produto: Produto, db: Session = Depends(get_db)):
    RepositorioProduto(db).editar(id, produto)
    produto.id = id
    return produto
