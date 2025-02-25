import os
import psycopg2
import pandas as pd
from src.parameter import *
from src.functions import *


# Example usage
folder_path = r'datos_a_db'
dataframes_list = load_csvs_to_dataframes(folder_path)

#tables_list = ['clientes', 'eventos', 'hoteles', 'hoteles_localizacion', 'reservas']  # List of table names corresponding to each DataFrame
tables_list = ['hoteles_localizacion', 'reservas']  # List of table names corresponding to each DataFrame

#print(dataframes_list)

# Iterate over the list of DataFrames and insert each one into the database
for df, tables in zip(dataframes_list, tables_list):
    print(df, "the tabla name is: ",tables)
    if tables == 'eventos':
        print(df.info())
        df = df.fillna(0)
        df['id_evento'] = pd.to_numeric(df['id_evento'], errors='coerce')
        df['id_evento'] = df['id_evento'].astype('int64')  # Para asegurarte de que es BIGINT
        df['codigo_postal'] = df['codigo_postal'].astype('int64')

    elif tables == 'hoteles':
        df = df.drop('fecha_reserva', axis=1)

        insert_dataframe_to_postgresql(tables, df, conn_params)
    else:
        insert_dataframe_to_postgresql(tables, df, conn_params)
    print(f"DataFrame inserted into table '{tables}' successfully.")


