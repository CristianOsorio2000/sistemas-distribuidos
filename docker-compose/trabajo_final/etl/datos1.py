import pandas as pd
import numpy as np

# Generar datos de muestra para la tabla X
data_x = {
    'id': np.arange(1, 101),
    'nombre': [f'Nombre_{i}' for i in range(1, 101)],
    'valor': np.random.randint(1, 100, size=100)
}

df_x = pd.DataFrame(data_x)
df_x.to_csv('datos1.csv', index=False)  # Cambiado a datos1.csv
print("Tabla X creada y guardada como datos1.csv")
