from fastapi import FastAPI
from pydantic import BaseModel
import mlflow.sklearn
import pandas as pd

app = FastAPI(title="API - Detección de Intrusiones de Red")

print("Cargando el modelo de Random Forest directamente desde la carpeta local...")

# Ruta relativa dentro del contenedor (ignora la base de datos y la ruta de Windows)
modelo_path = "mlruns/1/models/m-ca3e35af53684a3b978d3d6a98aa7491/artifacts"

# Cargar el modelo
modelo = mlflow.sklearn.load_model(modelo_path)
print("Modelo cargado exitosamente.")

class PaqueteRed(BaseModel):
    caracteristicas: list  # Cambiado a 'list' para aceptar los 78 ceros de tu prueba

@app.get("/")
def inicio():
    return {"mensaje": "Servicio de Detección de Intrusiones Activo"}

@app.post("/predecir")
def predecir_trafico(paquete: PaqueteRed):
    # Convierte la lista de 78 números en 1 fila de DataFrame
    df_entrada = pd.DataFrame([paquete.caracteristicas])
    prediccion = modelo.predict(df_entrada)
    estado = "Ataque detectado" if prediccion[0] == 1 else "Tráfico normal"
    
    return {
        "codigo_prediccion": int(prediccion[0]),
        "diagnostico": estado
    }