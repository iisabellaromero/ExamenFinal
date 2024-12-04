# 1.  Creación de Datos
## Script de Base de Datos: baseDeDatos.sql
Este script inicializa las tablas necesarias para gestionar los conciertos y tickets. Los campos y relaciones están diseñados para reflejar las dependencias entre los conciertos y sus tickets.


Concierto:

- id_concierto: Identificador único del concierto.
- nombre: Nombre del concierto.
- capacidad: Capacidad máxima de asistentes.
- fecha: Fecha y hora del concierto.

Ticket:

- id_ticket: Identificador único del ticket.
- id_concierto: Relación con la tabla concierto.
- dni: Identificación de la persona que adquiere el ticket.
- estado: Estado del ticket (disponible, vendido, cancelado).
- fecha_transaccion: Fecha de la transacción.


# 2. Integration Test (Base de Datos)
## Pruebas de CRUD usando Postman
Las siguientes capturas de Postman demuestran la funcionalidad de la API. Happy path y errores comunes se muestran en el contexto de un CRUD completo.
## POST /personas 

## GET /personas

## GET /conciertos: Recuperar la lista de conciertos.

## POST /tickets: Comprar un ticket.

## PUT /conciertos/{id}: Actualizar un concierto.

## DELETE /conciertos/{id}: Eliminar un concierto.

# 3. Código Completo de la API

El código de la API está disponible en el archivo main.py, junto con las definiciones de modelos y esquemas.

Elección de FastAPI
Se eligió FastAPI debido a:

- Simplicidad: Su sintaxis concisa y moderna acelera el desarrollo.
Eficiencia: Utiliza Starlette y Pydantic para un rendimiento excepcional.
Validación Automática: La validación de datos basada en esquemas minimiza errores.
Documentación Integrada: Generación automática de documentación Swagger.
Ejecución
Instalar dependencias:
bash
Copiar código
pip install fastapi uvicorn sqlalchemy
Iniciar servidor:
bash
Copiar código
uvicorn main:app --reload
4. Code Coverage
Resultados de Cobertura
Se utilizaron pytest y coverage.py para evaluar el código. El resultado final muestra una cobertura de 90%.

Reporte Resumido
bash
Copiar código
Name                        Stmts   Miss  Cover
-----------------------------------------------
app/main.py                   15      1    93%
app/routers/concierto.py      50      5    90%
app/routers/ticket.py         45      4    91%
-----------------------------------------------
TOTAL                        110     10    90%
Reporte HTML
Se generó un reporte HTML detallado (htmlcov/index.html) para identificar las líneas no cubiertas.

5. Endpoint Happy Path
Descripción del Happy Path
El endpoint POST /tickets/comprar se considera el happy path principal, ya que representa la operación más común: la compra de un ticket.

Flujo esperado:
Verifica la disponibilidad de boletos.
Registra un nuevo ticket si hay capacidad disponible.
Retorna una confirmación exitosa.
Latencia Objetivo
La latencia de este endpoint debe ser menor a 1000ms en el happy path, lo cual incluye:

Validación de la solicitud.
Consulta y actualización en la base de datos.
Obteniendo Datos de Latencia
Usamos JMeter para simular carga en el endpoint.
Ejemplo de prueba con 10 usuarios concurrentes:
Resultados de Latencia
El análisis mostró un tiempo promedio de respuesta de 850ms, cumpliendo con el objetivo de latencia.

# Performance testing: Load Testing
Propósito: Evaluar cómo el sistema maneja un número esperado de usuarios simultáneos o solicitudes dentro de condiciones normales.

# Teorema de CAP (C y P)
Consistencia (C): Todas las réplicas tienen los mismos datos en todo momento.
Disponibilidad (A): Cada solicitud recibe una respuesta, aunque los datos puedan no estar actualizados.
Tolerancia a particiones (P): El sistema continúa funcionando incluso si hay fallos de red que separan las réplicas.

# Logs agregados

