import pandas as pd

ruta_origen = "data/Clean_CICIDS2017.csv"
ruta_destino = "data/muestra_cicids.csv"

print("Cargando el dataset original de 1GB (esto tomará un minuto)...")

import random

# Probabilidad de saltarse una fila (90% de las veces la ignora, lee el 10%)
p_saltar = 0.90 

# Lee el archivo, manteniendo siempre el encabezado (fila 0), 
# y saltándose el resto de las filas basándose en la probabilidad aleatoria.
df = pd.read_csv(
    'data/Clean_CICIDS2017.csv', 
    skiprows=lambda i: i > 0 and random.random() < p_saltar
)

print("Extrayendo 50,000 registros aleatorios...")
# Extraer muestra aleatoria asegurando reproducibilidad
muestra = df.sample(n=50000, random_state=42)

print("Guardando la muestra ligera...")
muestra.to_csv(ruta_destino, index=False)
print("¡Listo! Muestra guardada en", ruta_destino)