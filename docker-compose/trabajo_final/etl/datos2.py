import pandas as pd
import numpy as np

# Generar datos de muestra para la tabla Y
data_y = {
    'id': np.arange(101, 201),
    'descripcion': [f'Descripcion_{i}' for i in range(101, 201)],
    'cantidad': np.random.randint(10, 500, size=100)
}

df_y = pd.DataFrame(data_y)
df_y.to_csv('datos2.csv', index=False)  # Cambiado a datos2.csv
print("Tabla Y creada y guardada como datos2.csv")
