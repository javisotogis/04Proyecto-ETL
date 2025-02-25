# Proyecto ETL: Análisis de Hoteles y Eventos en Madrid

## Descripción del Proyecto
Este proyecto es un proceso ETL (Extract, Transform, Load) que recopila y analiza datos de:
- **Reservas de hoteles:** Obtenidas de una base de datos.
- **Eventos en Madrid:** Recopilados a través de la API del Ayuntamiento de Madrid.
- **Precios de hoteles IBIS en Madrid:** Obtenidos mediante web scraping.

Los datos fueron transformados con la biblioteca **pandas** y cargados en una base de datos.

## Estructura de la Base de Datos
- **Tablas:**
  - `hoteles`: Información de los hoteles analizados.
  - `eventos`: Detalles de los eventos en Madrid.
  - `hoteles_localizacion`: Ubicación geográfica de los hoteles.
  - `clientes`: Datos de los clientes y sus reservas.
  - `ciudad`: Información general sobre Madrid.

- **Extensión PostGIS:** Utilizada para crear la geometría de puntos a partir de coordenadas (latitud y longitud) usando EPSG 4326.

- **Vistas:**
  - `eventos_rango`: Identifica eventos dentro del rango de las reservas.
  - `hoteles_recaudacion`: Muestra la recaudación de los hoteles según su categoría (competencia o no).

## Análisis y Consultas
Los archivos `bonus_track_1` y `bonus_track_2` contienen análisis y consultas SQL que permiten conocer:
- Número total de hoteles.
- Precio medio, máximo y mínimo de la competencia.
- Clientes con mayor gasto.

## Proceso ETL
### Archivos Principales
1. **`00_EDA_Hoteles.ipynb`**: Análisis exploratorio de datos en formato Parquet.
2. **`01_Extraccion_Web_Scraping.ipynb`**: Web scraping de precios y estrellas de 10 hoteles IBIS.
3. **`02_Extraccion_API.ipynb`**: Obtención de datos de eventos desde la API del Ayuntamiento.
4. **`03_Transformacion_Hoteles.ipynb`**: Preparación de tablas, creación de IDs y unión de hoteles propios y de la competencia.
5. **`04_Carga_a_BBDD.py`**: Carga de datos en la base de datos mediante funciones de la carpeta `SRC`.
6. **`05_Mapa.py`**: Muestra la localizacion de los datos.

### Estructura de Carpetas
- **`SRC`**: Contiene funciones para:
  - Subir datos a la base de datos usando `psycopg2`.
  - Convertir archivos CSV en dataframes.
- **`datos_a_db`**: Dataframes transformados listos para la carga.
- **`datos_entrada`**: Datos fuente, incluido el archivo Parquet de hoteles.

## Librerías Utilizadas
- `pandas`, `psycopg2`, `requests`, `beautifulsoup4`, `selenium`, `seaborn`, `matplotlib`, `geopandas`

## Seguridad
- El archivo `.gitignore` excluye las credenciales de la base de datos.

## Visualización Geoespacial
- Se generó un mapa con **GeoPandas** y **Matplotlib** para mostrar la ubicación de hoteles y eventos.
- Se conecta a la base de datos usando `psycopg2`.
- Se obtienen los datos de las tablas `hoteles_localizacion` y `eventos`.
- Los hoteles se muestran en azul con sus `id_hotel` como etiquetas.
- Los eventos se muestran en el mapa sin categorizar.
- Se generan los poligonos de Voronoi para determinar el area de influencia de los hoteles
- Los resultados de exportan en el archivo **Hoteles Influencia Area Mapa.**

Este código es multiplataforma y solo usa las bibliotecas solicitadas: **psycopg2**, **pandas**, **geopandas** y **matplotlib**.


## Contacto
¿Tienes preguntas o sugerencias? Contáctame a través de este repositorio de GitHub.

¡Gracias por consultar mi proyecto!

