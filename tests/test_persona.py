from fastapi.testclient import TestClient
from app.main import app
import pdb 

client = TestClient(app)

def test_create_persona():
    """Prueba para crear una persona."""
    nueva_persona = {
        "dni": "78778781",
        "nombre": "Juan",
        "apellido": "Pérez"
    }
    response = client.post("/personas/", json=nueva_persona)
    assert response.status_code == 200

def test_get_personas():
    """Prueba para obtener todas las personas."""
    response = client.get("/personas/")
    assert response.status_code == 200

def test_get_persona_by_dni_found():
    """Prueba para obtener una persona existente por DNI."""
    response = client.get("/personas/78778781")  # Cambia por un DNI que exista en tu base de datos
    # pdb.set_trace()
    assert response.status_code == 200

def test_get_persona_by_dni_not_found():
    """Prueba para intentar obtener una persona inexistente por DNI."""
    response = client.get("/personas/99993339999")  # DNI que no existe
    assert response.status_code == 404


