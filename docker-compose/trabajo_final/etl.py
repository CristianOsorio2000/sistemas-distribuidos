import pandas as pd
from sqlalchemy import create_engine
import cx_Oracle

# Conexión a las bases de datos PostgreSQL
engine_ppal = create_engine('postgresql://postgres_ppal:postgres_ppal@localhost:5432/db_ppal')
engine_slave1 = create_engine('postgresql://postgres_slave1:postgres_slave1@localhost:5433/db_slave1')

# Conexión a Oracle Data Warehouse
oracle_connection = cx_Oracle.connect(
    user="system",
    password="oracle",
    dsn="localhost:1521/xe"
)

# Cargar datos de PostgreSQL a Oracle Data Warehouse
def load_to_oracle(df, table_name):
    cursor = oracle_connection.cursor()
    for index, row in df.iterrows():
        cursor.execute(f"""
            INSERT INTO {table_name} (ID, NOMBRE, VALOR)
            VALUES (:1, :2, :3)""",
            (row['id'], row['nombre'], row['valor'])
        )
    oracle_connection.commit()
    cursor.close()

# Cargar datos de PostgreSQL
df_x = pd.read_csv('datos1.csv')
df_y = pd.read_csv('datos2.csv')

df_x.to_sql('tabla_x', engine_ppal, if_exists='replace')
df_y.to_sql('tabla_y', engine_slave1, if_exists='replace')

# Cargar datos a Oracle Data Warehouse
load_to_oracle(df_x, 'TABLA_X')
load_to_oracle(df_y, 'TABLA_Y')

oracle_connection.close()

