from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_comprar_ticket():
    # Datos para la prueba
    nuevo_ticket = {
        "id_concierto": 1,
        "dni": "74450872",
        "estado": "vendido",
        "fecha_transaccion": "2024-12-03T15:00:00"
    }
    
    # Simula la solicitud POST al endpoint
    response = client.post("/tickets", json=nuevo_ticket)

    # Asegura que el código de respuesta sea 200
    assert response.status_code == 200
    
    # Asegura que la respuesta contiene datos
    assert response.json()


def test_comprar_ticket_concierto_no_existente():
    # Datos para la prueba
    nuevo_ticket = {
        "id_concierto": 9999,  # ID de concierto inexistente
        "dni": "74450872",
        "estado": "vendido",
        "fecha_transaccion": "2024-12-03T15:00:00"
    }
    
    # Simula la solicitud POST al endpoint
    response = client.post("/tickets", json=nuevo_ticket)

    # Asegura que el código de respuesta sea 404
    assert response.status_code == 404
    
    # Asegura que el mensaje esperado esté en la respuesta
    # assert response.json() == {"detail": "Concierto no encontrado"}


def test_comprar_ticket_datos_invalidos():
    # Datos inválidos: falta el estado del ticket
    nuevo_ticket = {
        "id_concierto": 1,
        "dni": "74450872",
        "fecha_transaccion": "2024-12-03T15:00:00"
    }
    
    # Simula la solicitud POST al endpoint
    response = client.post("/tickets", json=nuevo_ticket)

    # Asegura que el código de respuesta sea 422
    assert response.status_code == 422  # Error de validación
    
    # Asegura que la respuesta contiene errores de validación
    # assert "detail" in response.json()


# def test_comprar_ticket_concierto_lleno():
#     # Simula que el concierto con id=1 está lleno
#     nuevo_ticket = {
#         "id_concierto": 1,  # Concierto con capacidad alcanzada
#         "dni": "74450872",
#         "estado": "vendido",
#         "fecha_transaccion": "2024-12-03T15:00:00"
#     }
    
#     # Simula la solicitud POST al endpoint
#     response = client.post("/tickets", json=nuevo_ticket)

#     # Asegura que el código de respuesta sea 400
#     assert response.status_code == 400  # Capacidad alcanzada
    
#     # Asegura que el mensaje esperado esté en la respuesta
#     # assert response.json() == {"detail": "El concierto ya alcanzó su capacidad máxima"}

def test_obtener_all_tickets():
    # Simula la solicitud GET al endpoint
    response = client.get("/tickets")

    # Asegura que el código de respuesta sea 200
    assert response.status_code == 200
    
    # Asegura que la respuesta contiene datos
    assert response.json()
