from sqlalchemy import Column, Integer, String, Boolean, Date
from database import Base

class Tarefa(Base):
    __tablename__ = "tarefas"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    descricao = Column(String)
    disciplina = Column(String)
    data_entrega = Column(Date)
    concluida = Column(Boolean, default=False)
