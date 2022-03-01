from sqlalchemy import select
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sql.models import models

class RepositorioUsuario():
    def __init__(self, session: Session):
        self.session = session

    def criar(self, usuario: schemas.Usuario):
        bd_usuario = models.Usuario(nome = usuario.nome,
                                    senha = usuario.senha,
                                    telefone = usuario.telefone,
                                    produtos = usuario.produtos)
        self.session.add(bd_usuario)
        self.session.commit()
        self.session.refresh(bd_usuario)
        return bd_usuario

    def listar(self):
        stmt = select(models.Usuario)
        usuarios = self.session.execute(stmt).scalars().all()
        return usuarios

    def obter(self):
        pass

    def remover(self):
        pass
