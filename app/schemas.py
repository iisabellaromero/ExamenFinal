from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List
from app.models import TicketEstado

class ConciertoBase(BaseModel):
    nombre: str
    capacidad: int
    fecha: datetime

class ConciertoCreate(ConciertoBase):
    pass

class Concierto(ConciertoBase):
    id_concierto: int

    class Config:
        orm_mode = True

class PersonaBase(BaseModel):
    dni: str
    nombre: str
    apellido: str

class PersonaCreate(PersonaBase):
    pass

class Persona(PersonaBase):
    class Config:
        orm_mode = True

class TicketBase(BaseModel):
    id_concierto: int
    dni: Optional[str]
    estado: TicketEstado
    fecha_transaccion: datetime

class TicketCreate(TicketBase):
    pass

class Ticket(TicketBase):
    id_ticket: int

    class Config:
        orm_mode = True
