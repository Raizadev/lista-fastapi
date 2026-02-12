from pydantic import BaseModel
from datetime import date

class TarefaBase(BaseModel):
    titulo: str
    descricao: str
    disciplina: str
    data_entrega: date

class TarefaCreate(TarefaBase):
    pass

class Tarefa(TarefaBase):
    id: int
    concluida: bool

    class Config:
        orm_mode = True
