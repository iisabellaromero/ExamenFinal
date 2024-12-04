from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db

router = APIRouter(prefix="/personas", tags=["Personas"])

@router.post("/", response_model=schemas.Persona)
def create_persona(persona: schemas.PersonaCreate, db: Session = Depends(get_db)):
    db_persona = models.Persona(**persona.dict())
    db.add(db_persona)
    db.commit()
    db.refresh(db_persona)
    return db_persona

@router.get("/", response_model=List[schemas.Persona])
def list_personas(db: Session = Depends(get_db)):
    return db.query(models.Persona).all()

@router.get("/{dni}", response_model=schemas.Persona)
def get_persona(dni: str, db: Session = Depends(get_db)):
    persona = db.query(models.Persona).filter(models.Persona.dni == dni).first()
    if not persona:
        raise HTTPException(status_code=404, detail="Persona not found")
    return persona

@router.delete("/{dni}")
def delete_persona(dni: str, db: Session = Depends(get_db)):
    db_persona = db.query(models.Persona).filter(models.Persona.dni == dni).first()
    if not db_persona:
        raise HTTPException(status_code=404, detail="Persona not found")
    db.delete(db_persona)
    db.commit()
    return {"message": "Persona deleted successfully"}
