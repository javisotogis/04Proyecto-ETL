-- Cambiar 0 por nulos en el codigo postal
UPDATE public.eventos set organizacion = null where organizacion = '0';
UPDATE public.eventos set codigo_postal = null where codigo_postal = 0;
UPDATE public.eventos set direccion = null where direccion = '0';
UPDATE public.eventos set codigo_postal = null where codigo_postal = 0;
UPDATE public.eventos set horario = null where horario = '0';

-- Cuantos hoteles tiene la base de datos
SELECT competencia, count(*) as numero_hoteles from hoteles
group by competencia; --19 propios y 10 competencia

-- Cuantas reservas se han hecho
SELECT count (*) FROM public.reservas; --15000

-- Identifica los 10 clientes que más se han gastado
SELECT id_cliente, SUM(precio_noche) as gasto_cliente FROM public.reservas group by id_cliente
ORDER by SUM(precio_noche) DESC
limit 10;


-- Identifica el hotel de la competencia y el hotel de nuestra marca que más han recaudado para esas fechas
CREATE VIEW hoteles_recaudacion AS 
SELECT r.id_hotel, SUM(round(precio_noche::numeric,2)), h.competencia
FROM reservas r
JOIN hoteles h
on r.id_hotel = h.id_hotel
group by r.id_hotel, h.competencia
order by SUM(round(precio_noche::numeric,2));

SELECT DISTINCT ON (competencia) competencia, id_hotel, sum
FROM hoteles_recaudacion
ORDER BY competencia, sum DESC;


-- Identifica cuantos eventos hay.

CREATE VIEW eventos_rango AS SELECT DISTINCT e.*
FROM eventos e
JOIN reservas r ON e.fecha_inicio <= r.final_estancia 
               AND e.fecha_fin >= r.inicio_estancia;

-- Identifica el día que más reservas se han hecho para nuestro hoteles
-- No puedo hacerlo por que he puesto la misma fecha para todas las reservas por error, he cogido la fehca de reserva para los hoteles de la competencia. No obstante esto seria:
SELECT fecha_reserva, count(*) from reservas
GROUP BY fecha_reserva
order by count(*) DESC
limit 1;

-- Una vez creada la base de datos haz una o varias consultas para crear un 
-- dataframe con los datos relevantes para hacer un análisis de precios entre la competencia y 
-- nuestros hoteles para esas fechas.

SELECT competencia,
       ROUND(AVG(sum::NUMERIC), 2) AS precio_medio,
       ROUND(SUM(sum::NUMERIC), 2) AS total_recaudacion,
       ROUND(MAX(sum::NUMERIC), 2) AS max_recaudacion,
       ROUND(MIN(sum::NUMERIC), 2) AS min_recaudacion,
       COUNT(*) AS total_hoteles
FROM hoteles_recaudacion
GROUP BY competencia
ORDER BY competencia;


-- Realiza un análisis temporal de las fechas de reserva
-- No puedo hacerlo por que he puesto la misma fecha para todas las reservas por error, 
--he cogido la fehca de reserva para los hoteles de la competencia.




