from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db
import logging
from datetime import datetime
router = APIRouter(prefix="/personas", tags=["Personas"])

# Configuración del logger
fecha_actual = datetime.now().strftime("%d_%m_%Y")
logging.basicConfig(
    filename=f"log_{fecha_actual}.log",  # Nombre del archivo
    level=logging.INFO,  # Nivel de logging
    format="%(asctime)s - %(levelname)s - %(message)s",  # Formato del log
)

@router.post("/", response_model=schemas.Persona)
def create_persona(persona: schemas.PersonaCreate, db: Session = Depends(get_db)):
    try:
        # Lógica para crear la persona
        #chequear q el dni no este en la bd:
        db_persona = db.query(models.Persona).filter(models.Persona.dni == persona.dni).first()
        if db_persona:
            raise HTTPException(status_code=409, detail="Persona already exists")
        db_persona = models.Persona(**persona.dict())
        db.add(db_persona)
        db.commit()
        db.refresh(db_persona)

        # Registrar éxito en el log
        logging.info("Éxito en ejecución: Persona creada con éxito")
        return db_persona
    except Exception as e:
        # Registrar error en el log
        logging.error(f"Error en ejecución: {str(e)}")
        raise HTTPException(status_code=500, detail="Error interno del servidor")

@router.get("/", response_model=list[schemas.Persona])
def list_personas(db: Session = Depends(get_db)):
    return db.query(models.Persona).all()

@router.get("/{dni}", response_model=schemas.Persona)
def get_persona(dni: str, db: Session = Depends(get_db)):
    persona = db.query(models.Persona).filter(models.Persona.dni == dni).first()
    if not persona:
        #404: Not found
        raise HTTPException(status_code=404, detail="Persona not found")
    return persona

@router.delete("/{dni}")
def delete_persona(dni: str, db: Session = Depends(get_db)):
    db_persona = db.query(models.Persona).filter(models.Persona.dni == dni).first()
    if not db_persona:
        #404 Not found:
        raise HTTPException(status_code=404, detail="Persona not found")
    db.delete(db_persona)
    db.commit()
    return {"message": "Persona deleted successfully"}

