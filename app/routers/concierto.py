from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db
from typing import List

router = APIRouter(prefix="/conciertos", tags=["Conciertos"])

@router.post("/", response_model=schemas.Concierto)
def create_concierto(concierto: schemas.ConciertoCreate, db: Session = Depends(get_db)):
    db_concierto = models.Concierto(**concierto.dict())
    db.add(db_concierto)
    db.commit()
    db.refresh(db_concierto)
    return db_concierto

@router.get("/", response_model=list[schemas.Concierto])
def list_conciertos(db: Session = Depends(get_db)):
    return db.query(models.Concierto).all()

@router.get("/{concierto_id}", response_model=schemas.Concierto)
def get_concierto(concierto_id: int, db: Session = Depends(get_db)):
    concierto = db.query(models.Concierto).filter(models.Concierto.id_concierto == concierto_id).first()
    if not concierto:
        raise HTTPException(status_code=404, detail="Concierto not found")
    return concierto

@router.put("/{concierto_id}", response_model=schemas.Concierto)
def update_concierto(concierto_id: int, concierto: schemas.ConciertoCreate, db: Session = Depends(get_db)):
    db_concierto = db.query(models.Concierto).filter(models.Concierto.id_concierto == concierto_id).first()
    if not db_concierto:
        raise HTTPException(status_code=404, detail="Concierto not found")
    db_concierto.nombre = concierto.nombre
    db_concierto.capacidad = concierto.capacidad
    db_concierto.fecha = concierto.fecha
    db.commit()
    db.refresh(db_concierto)
    return db_concierto

@router.delete("/{concierto_id}")
def delete_concierto(concierto_id: int, db: Session = Depends(get_db)):
    db_concierto = db.query(models.Concierto).filter(models.Concierto.id_concierto == concierto_id).first()
    if not db_concierto:
        raise HTTPException(status_code=404, detail="Concierto not found")
    db.delete(db_concierto)
    db.commit()
    return {"message": "Concierto deleted successfully"}

