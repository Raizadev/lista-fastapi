from sqlalchemy.orm import Session
import models, schemas

def criar_tarefa(db: Session, tarefa: schemas.TarefaCreate):
    db_tarefa = models.Tarefa(**tarefa.dict())
    db.add(db_tarefa)
    db.commit()
    db.refresh(db_tarefa)
    return db_tarefa

def listar_tarefas(db: Session):
    return db.query(models.Tarefa).all()

def concluir_tarefa(db: Session, tarefa_id: int):
    tarefa = db.query(models.Tarefa).filter(models.Tarefa.id == tarefa_id).first()
    if tarefa:
        tarefa.concluida = True
        db.commit()
        db.refresh(tarefa)
    return tarefa

def apagar_tarefa(db: Session, tarefa_id: int):
    tarefa = db.query(models.Tarefa).filter(models.Tarefa.id == tarefa_id).first()
    
    if not tarefa:
        return None

    db.delete(tarefa)
    db.commit()
    return tarefa
