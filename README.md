https://github.com/iisabellaromero/ExamenFinal

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

![Post method](https://github.com/iisabellaromero/ExamenFinal/tree/main/images/post.png?raw=true)

![404](https://github.com/iisabellaromero/ExamenFinal/tree/main/images/404.png?raw=true)




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
Se utilizaron pytest y coverage.py para evaluar el código. El resultado final muestra una cobertura de 85% 
![coverage](https://github.com/iisabellaromero/ExamenFinal/tree/main/images/coverage.png?raw=true)




5. Endpoint Happy Path
=El endpoint POST /tickets se considera el happy path principal, ya que representa la operación más común: la compra de un ticket.

Flujo esperado:
Verifica la disponibilidad de boletos.
Registra un nuevo ticket si hay capacidad disponible.
Retorna una confirmación exitosa.

Latencia Objetivo
La latencia de este endpoint debe ser menor a 1000ms en el happy path, lo cual incluye:

- Validación de la solicitud.
- Consulta y actualización en la base de datos.
- Obteniendo Datos de Latencia
![latency](https://github.com/iisabellaromero/ExamenFinal/tree/main/images/latency.png?raw=true )

### Usamos JMeter para simular carga en el endpoint.
Ejemplo de prueba con 10 usuarios concurrentes, con Ramp up de 10 segundos y loop count de 10 
![jmeter](https://github.com/iisabellaromero/ExamenFinal/tree/main/images/jmeter2.png?raw=true )


# Performance testing: Load Testing
Propósito: Evaluar cómo el sistema maneja un número esperado de usuarios simultáneos o solicitudes dentro de condiciones normales.

# Teorema de CAP (C y P)
Consistencia (C): Todas las réplicas tienen los mismos datos en todo momento.
Disponibilidad (A): Cada solicitud recibe una respuesta, aunque los datos puedan no estar actualizados.
Tolerancia a particiones (P): El sistema continúa funcionando incluso si hay fallos de red que separan las réplicas.

# Logs agregados

Agregamos un Log Parser script para poder procesar los logs del file segun la fecha

![log](https://github.com/iisabellaromero/ExamenFinal/tree/main/images/logfile.png?raw=true)

![log2](https://github.com/iisabellaromero/ExamenFinal/tree/main/images/logparser.png?raw=true )
