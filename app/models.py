from sqlalchemy import Column, Integer, String, Enum, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import Base
import enum

class TicketEstado(str, enum.Enum):
    disponible = "disponible"
    vendido = "vendido"
    cancelado = "cancelado"

class Concierto(Base):
    __tablename__ = "concierto"

    id_concierto = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), nullable=False)
    capacidad = Column(Integer, nullable=False)
    fecha = Column(DateTime, nullable=False)

    tickets = relationship("Ticket", back_populates="concierto")

class Persona(Base):
    __tablename__ = "persona"

    dni = Column(String(20), primary_key=True, index=True)
    nombre = Column(String(255), nullable=False)
    apellido = Column(String(255), nullable=False)

    tickets = relationship("Ticket", back_populates="persona")

class Ticket(Base):
    __tablename__ = "ticket"

    id_ticket = Column(Integer, primary_key=True, index=True)
    id_concierto = Column(Integer, ForeignKey("concierto.id_concierto"), nullable=False)
    dni = Column(String(20), ForeignKey("persona.dni"), nullable=True)
    estado = Column(Enum(TicketEstado), nullable=False)
    fecha_transaccion = Column(DateTime, nullable=False)

    concierto = relationship("Concierto", back_populates="tickets")
    persona = relationship("Persona", back_populates="tickets")
