# Proyecto ETL: Análisis de Reservas de Hotel

## Descripción del Proyecto
Este proyecto tiene como objetivo realizar un proceso ETL (Extract, Transform, Load) utilizando la biblioteca **Pandas** para analizar un archivo en formato **Parquet** que contiene información sobre reservas de hotel.

## Proceso de Análisis Exploratorio de Datos (EDA)
Durante el análisis exploratorio de datos (EDA), se llevaron a cabo las siguientes acciones:

- **Limpieza de Datos:** Se realizó la limpieza de datos para garantizar la calidad de la información.
- **Generación de IDs Únicos:** Se crearon identificadores únicos para los clientes y los nombres de los hoteles.
- **Hallazgos Relevantes:** Se identificó que el archivo de origen no contiene información sobre los hoteles de la competencia.

## Obtención de Información Adicional
Para complementar la información faltante, se emplearon las siguientes fuentes externas:

- **Web de Ibis Madrid:** Se realizó un proceso de web scraping para obtener datos sobre los hoteles de la competencia.
- **API del Ayuntamiento de Madrid:** Se consultaron los eventos ocurridos en las fechas correspondientes a las reservas.

Esta información adicional se integró en el proceso ETL para enriquecer el análisis y ofrecer una visión más completa del contexto de las reservas.
