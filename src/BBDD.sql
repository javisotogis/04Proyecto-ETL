-- Extensión para usar UUID
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

CREATE TABLE ciudad (
    id_ciudad UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    nombre_ciudad TEXT
);

CREATE TABLE eventos (
    id_evento UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    nombre_evento TEXT,
    url_evento TEXT,
    codigo_postal INT,
    direccion TEXT,
    horario TEXT,
    organizacion TEXT,
    id_ciudad UUID REFERENCES ciudad(id_ciudad) ON DELETE CASCADE
);

CREATE TABLE hoteles (
    id_hotel UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    nombre_hotel TEXT,
    estrellas INT CHECK (estrellas BETWEEN 1 AND 5),
    id_ciudad UUID REFERENCES ciudad(id_ciudad) ON DELETE CASCADE
);

CREATE TABLE clientes (
    id_cliente UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    nombre TEXT,
    apellido TEXT,
    mail TEXT UNIQUE CHECK (mail LIKE '%@%')
);

CREATE TABLE reservas (
    id_reserva UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    fecha_reserva DATE,
    inicio_estancia DATE,
    final_estancia DATE,
    precio_noche FLOAT CHECK (precio_noche >= 0),
    id_cliente UUID REFERENCES clientes(id_cliente) ON DELETE CASCADE,
    id_hotel UUID REFERENCES hoteles(id_hotel) ON DELETE CASCADE
);
