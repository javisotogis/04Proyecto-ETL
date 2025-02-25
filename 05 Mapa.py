# Código para crear un mapa en Python usando Matplotlib, GeoPandas y Voronoi
# Mostrando la localización de hoteles con etiquetas, eventos y polígonos de Voronoi con zoom limitado a la extensión de hoteles y eventos.

import psycopg2
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon
from scipy.spatial import Voronoi
import numpy as np

from src.parameter import *

# Función para obtener datos de la base de datos
def get_data_from_db(query, db_config):
    with psycopg2.connect(**db_config) as conn:
        df = pd.read_sql(query, conn)
    return df

# Configuración de la base de datos
DB_CONFIG = {
    'dbname': database_name,
    'user': user,
    'password': password,
    'host': host,
    'port': 5433
}

# Consulta SQL para hoteles y eventos
query_hoteles = "SELECT id_hotel, latitud, longitud FROM hoteles_localizacion;"
query_eventos = "SELECT latitud, longitud FROM eventos_rango;"

# Obtener los datos
df_hoteles = get_data_from_db(query_hoteles, DB_CONFIG)
df_eventos = get_data_from_db(query_eventos, DB_CONFIG)

# Eliminar filas inválidas
df_hoteles = df_hoteles.dropna().query("latitud != 0 and longitud != 0")
df_eventos = df_eventos.dropna().query("latitud != 0 and longitud != 0")

# Convertir a GeoDataFrames
gdf_hoteles = gpd.GeoDataFrame(df_hoteles, geometry=gpd.points_from_xy(df_hoteles.longitud, df_hoteles.latitud))
gdf_eventos = gpd.GeoDataFrame(df_eventos, geometry=gpd.points_from_xy(df_eventos.longitud, df_eventos.latitud))

# Calcular polígonos de Voronoi
points = np.array(list(zip(gdf_hoteles.geometry.x, gdf_hoteles.geometry.y)))
vor = Voronoi(points)

# Crear polígonos a partir de las regiones de Voronoi
def voronoi_polygons(vor):
    polygons = []
    for region in vor.regions:
        if not region or -1 in region:
            continue
        polygon = Polygon([vor.vertices[i] for i in region])
        polygons.append(polygon)
    return polygons

vor_polygons = voronoi_polygons(vor)
gdf_voronoi = gpd.GeoDataFrame(geometry=vor_polygons)

# Crear el mapa
fig, ax = plt.subplots(figsize=(10, 8))

# Ajustar el zoom al área de hoteles y eventos
bounds = pd.concat([gdf_hoteles.geometry, gdf_eventos.geometry]).total_bounds
ax.set_xlim(bounds[0] - 0.01, bounds[2] + 0.01)
ax.set_ylim(bounds[1] - 0.01, bounds[3] + 0.01)

# Dibujar los polígonos de Voronoi
gdf_voronoi.plot(ax=ax, cmap='tab20', alpha=0.5, edgecolor='black')

# Graficar hoteles con etiquetas
gdf_hoteles.plot(ax=ax, color='blue', marker='o')
for _, row in gdf_hoteles.iterrows():
    ax.annotate(text=str(row['id_hotel']), xy=(row.geometry.x, row.geometry.y), fontsize=8, ha='center', va='center')

# Graficar eventos
gdf_eventos.plot(ax=ax, color='red', marker='x')

# Mostrar el mapa
plt.title('Mapa de Hoteles, Eventos y Polígonos de Voronoi (Zoom Limitado)')
plt.xlabel('Longitud')
plt.ylabel('Latitud')
plt.show()
