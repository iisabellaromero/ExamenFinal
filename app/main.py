from fastapi import FastAPI
from app.database import engine, Base
from app.routers import concierto, persona, ticket

app = FastAPI()

# Crear tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Registrar rutas
app.include_router(concierto.router)
app.include_router(persona.router)
app.include_router(ticket.router)

@app.get("/")
def root():
    return {"message": "Bienvenido a la API de gestión de conciertos"}
