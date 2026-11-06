import requests
import pandas as pd

print("Extrayendo un paquete de red real del dataset...")
df = pd.read_csv("data/muestra_cicids.csv").fillna(0)
# Seleccionamos solo las variables numéricas (lo que espera el modelo)
X = df.iloc[:, :-1].select_dtypes(include=['float64', 'int64'])

# Tomar la primera fila y convertirla en el diccionario esperado
paquete_prueba = X.iloc[0].to_dict()

print("Enviando petición a la API de FastAPI...")
url = "http://127.0.0.1:8000/predecir"

# FastAPI espera un JSON con la estructura {"caracteristicas": {datos...}}
respuesta = requests.post(url, json={"caracteristicas": paquete_prueba})

print("\n=== DIAGNÓSTICO DEL IDS ===")
print(respuesta.json())