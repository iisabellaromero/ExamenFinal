from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_conciertos():
    response = client.get("/conciertos/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_concierto():
    nuevo_concierto = {
        "nombre": "Concierto de Prueba",
        "capacidad": 5000,
        "fecha": "2024-12-31T20:00:00"
    }
    response = client.post("/conciertos/", json=nuevo_concierto)
    assert response.status_code == 200
    assert response.json()["nombre"] == "Concierto de Prueba"


def test_get_concierto_not_found():
    response = client.get("/conciertos/9999")  # Un ID que no existe
    assert response.status_code == 404
    # assert response.json() == {"detail": "Concierto no encontrado"}
