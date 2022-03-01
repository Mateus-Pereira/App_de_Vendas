from fastapi import APIRouter, status, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from src.infra.sql.config.database import get_db
from src.schemas.schemas import Pedido


router = APIRouter()

@router.post('/pedidos', status_code=status.HTTP_201_CREATED, response_model=Pedido)
def fazer_pedido(pedido: Pedido, db: Session = Depends(get_db)):
    pass

@router.get('/pedidos/{id}', response_model=Pedido)
def exibir_pedido(id: int, db: Session = Depends(get_db)):
    pass

@router.get('/pedidos', response_model=[Pedido])
def listar_pedido(db: Session = Depends(get_db)):
    pass