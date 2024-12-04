from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db

router = APIRouter(prefix="/tickets", tags=["Tickets"])

@router.post("/", response_model=schemas.Ticket)
def create_ticket(ticket: schemas.TicketCreate, db: Session = Depends(get_db)):
    #only the id_concierto exists in db
    db_concierto = db.query(models.Concierto).filter(models.Concierto.id_concierto == ticket.id_concierto).first()
    if not db_concierto:
        raise HTTPException(status_code=404, detail="Concierto not found")
    #Only if dni exists in db
    if ticket.dni:
        db_persona = db.query(models.Persona).filter(models.Persona.dni == ticket.dni).first()
        if not db_persona:
            raise HTTPException(status_code=404, detail="Persona not found")

    db_ticket = models.Ticket(**ticket.dict())
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket

@router.get("/", response_model=list[schemas.Ticket])
def list_tickets(db: Session = Depends(get_db)):
    return db.query(models.Ticket).all()

@router.put("/{ticket_id}", response_model=schemas.Ticket)
def update_ticket(ticket_id: int, ticket: schemas.TicketCreate, db: Session = Depends(get_db)):
    db_ticket = db.query(models.Ticket).filter(models.Ticket.id_ticket == ticket_id).first()
    if not db_ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    for key, value in ticket.dict().items():
        setattr(db_ticket, key, value)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket

@router.delete("/{ticket_id}")
def delete_ticket(ticket_id: int, db: Session = Depends(get_db)):
    db_ticket = db.query(models.Ticket).filter(models.Ticket.id_ticket == ticket_id).first()
    if not db_ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    db.delete(db_ticket)
    db.commit()
    return {"message": "Ticket deleted successfully"}
