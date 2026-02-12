from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Lista de Tarefas Académicas")

# Dependência da base de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/tarefas/", response_model=schemas.Tarefa)
def criar_tarefa(tarefa: schemas.TarefaCreate, db: Session = Depends(get_db)):
    return crud.criar_tarefa(db, tarefa)

@app.get("/tarefas/", response_model=list[schemas.Tarefa])
def listar_tarefas(db: Session = Depends(get_db)):
    return crud.listar_tarefas(db)

@app.put("/tarefas/{tarefa_id}/concluir")
def concluir_tarefa(tarefa_id: int, db: Session = Depends(get_db)):
    tarefa = crud.concluir_tarefa(db, tarefa_id)
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return tarefa

@app.delete("/tarefas/{tarefa_id}")
def apagar_tarefa(tarefa_id: int, db: Session = Depends(get_db)):
    tarefa = crud.apagar_tarefa(db, tarefa_id)

    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    return {"mensagem": "Tarefa apagada com sucesso"}

