from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.infra.sql.config.database import Base


class Usuario(Base):

    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    senha = Column(String)
    telefone = Column(String)

    produtos = relationship('Produto', back_populates='usuario')
    pedido = relationship('Pedido', back_populates='produtos')


class Produto(Base):

    __tablename__ = 'produto'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    descricao = Column(String)
    preco = Column(Float)
    disponivel = Column(Boolean)
    tamanhos = Column(String)
    usuario_id = Column(Integer, ForeignKey('usuario.id', name='ID_usuario'))

    usuario = relationship('Usuario', back_populates='produtos')
    

class Pedido(Base):
    __tablename__ = 'Pedidos'

    id = Column(Integer, primary_key = True, index = True)
    quantdade = Column(Integer)
    local_entrega = Column(String)
    tipo_entrega = Column(String)
    observacao = Column(String)

    usuario_id = Column(Integer, ForeignKey('usuario.id', name='ID_pedido_usuario'))
    produto_id = Column(Integer, ForeignKey('produto.id', name='ID_pedido_produto'))

    usuario = relationship('Usuario', back_populates='pedidos')
    produto = relationship('Produto')