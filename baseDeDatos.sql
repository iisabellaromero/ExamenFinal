-- Crear la base de datos (opcional)
CREATE DATABASE sistema_conciertos;
\c sistema_conciertos -- Conectar a la base de datos

-- Crear la tabla 'concierto'
CREATE TABLE concierto (
    id_concierto SERIAL PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    capacidad INT NOT NULL,
    fecha TIMESTAMP NOT NULL
);

-- Crear la tabla 'persona'
CREATE TABLE persona (
    dni VARCHAR(20) PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL
);

-- Crear la tabla 'ticket'
CREATE TABLE ticket (
    id_ticket SERIAL PRIMARY KEY,
    id_concierto INT NOT NULL,
    dni VARCHAR(20) NOT NULL,
    estado VARCHAR(20) CHECK (estado IN ('disponible', 'vendido', 'cancelado')),
    fecha_transaccion TIMESTAMP NOT NULL,
    CONSTRAINT fk_concierto FOREIGN KEY (id_concierto) REFERENCES concierto (id_concierto) ON DELETE CASCADE,
    CONSTRAINT fk_persona FOREIGN KEY (dni) REFERENCES persona (dni) ON DELETE CASCADE
);
