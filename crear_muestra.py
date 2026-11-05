import pandas as pd

ruta_origen = "data/Clean_CICIDS2017.csv"
ruta_destino = "data/muestra_cicids.csv"

print("Cargando el dataset original de 1GB (esto tomará un minuto)...")
df = pd.read_csv(ruta_origen)

print("Extrayendo 50,000 registros aleatorios...")
# Extraer muestra aleatoria asegurando reproducibilidad
muestra = df.sample(n=50000, random_state=42)

print("Guardando la muestra ligera...")
muestra.to_csv(ruta_destino, index=False)
print("¡Listo! Muestra guardada en", ruta_destino)