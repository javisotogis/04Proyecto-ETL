def insert_dataframe_to_postgresql(table_name, dataframe, conn_params):
    """
    Inserts a pandas DataFrame into a PostgreSQL table.

    Parameters:
    table_name (str): Name of the target table in PostgreSQL.
    dataframe (pd.DataFrame): DataFrame to be inserted.
    conn_params (dict): Dictionary containing connection parameters with keys:
                        'dbname', 'user', 'password', 'host', 'port'.
    """
    # Establish connection to PostgreSQL
    conn = psycopg2.connect(**conn_params)
    cursor = conn.cursor()

    # Create insert query dynamically based on DataFrame columns
    columns = ', '.join(dataframe.columns)
    values = ', '.join(['%s'] * len(dataframe.columns))
    insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"

    # Insert DataFrame rows into PostgreSQL table
    for row in dataframe.itertuples(index=False, name=None):
        cursor.execute(insert_query, row)

    # Commit changes and close connection
    conn.commit()
    cursor.close()
    conn.close()

# Example usage
conn_params = {
    'dbname': database_name,
    'user': user,
    'password': password,
    'host': host,
    'port': port
}

# Assuming df is your DataFrame
# insert_dataframe_to_postgresql('your_table_name', df, conn_params)


def load_csvs_to_dataframes(folder_path):
    """
    Loops through all CSV files in a given folder, loads each into a pandas DataFrame,
    and returns a list of DataFrames.

    Parameters:
    folder_path (str): The path to the folder containing the CSV files.

    Returns:
    list: A list of pandas DataFrames, each corresponding to a CSV file in the folder.
    """
    dataframes = []  # Initialize an empty list to store DataFrames
    
    # Loop through each file in the specified folder
    for filename in os.listdir(folder_path):
        # Check if the file is a CSV file
        if filename.endswith('.csv'):
            # Construct the full file path
            file_path = os.path.join(folder_path, filename)
            
            # Load the CSV file into a pandas DataFrame
            df = pd.read_csv(file_path)
            
            # Append the DataFrame to the list
            dataframes.append(df)
            
    return dataframes  # Return the list of DataFrames
