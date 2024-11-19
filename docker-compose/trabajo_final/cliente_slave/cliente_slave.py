from sqlalchemy import create_engine
import pandas as pd

# Conexión a la base de datos esclavo
engine_slave1 = create_engine('postgresql://postgres_slave1:postgres_slave1@pg_slave1:5433/db_slave1')

# Consulta a la base de datos
query = "SELECT * FROM tabla_y"
df_y = pd.read_sql_query(query, engine_slave1)

# Mostrar resultados
print(df_y.head())
