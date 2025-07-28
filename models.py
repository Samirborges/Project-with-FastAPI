from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base

db = create_engine("sqlite:///banco.db")

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    senha = Column("senha", String, nullable=False)
    email = Column("email", String, nullable=False)
    ativo = Column("ativo", Boolean)
    admin = Column("admin", Boolean)