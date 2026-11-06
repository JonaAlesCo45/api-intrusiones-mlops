from fastapi import FastAPI
from pydantic import BaseModel
import mlflow.sklearn
import mlflow
import pandas as pd

app = FastAPI(title="API - Detección de Intrusiones de Red")

print("Conectando con MLflow para buscar un modelo válido...")

# FILTRO CLAVE: Buscar solo ejecuciones donde la precisión (accuracy) sea mayor a 0
ejecuciones = mlflow.search_runs(
    experiment_names=["Deteccion_Intrusiones_Red"],
    filter_string="metrics.accuracy > 0",
    order_by=["start_time DESC"]
)

if ejecuciones.empty:
    raise Exception("No se encontró ningún modelo exitoso. Ejecuta entrenar_modelo.py de nuevo.")

# Ahora es completamente seguro tomar el primer elemento (el más reciente y exitoso)
run_id = ejecuciones.iloc[0].run_id
modelo_uri = f"runs:/{run_id}/modelo_rf"

# Cargar el modelo
modelo = mlflow.sklearn.load_model(modelo_uri)
print(f"Modelo cargado exitosamente desde la ejecución: {run_id}")

class PaqueteRed(BaseModel):
    caracteristicas: dict

@app.get("/")
def inicio():
    return {"mensaje": "Servicio de Detección de Intrusiones Activo"}

@app.post("/predecir")
def predecir_trafico(paquete: PaqueteRed):
    df_entrada = pd.DataFrame([paquete.caracteristicas])
    prediccion = modelo.predict(df_entrada)
    estado = "Ataque detectado" if prediccion[0] == 1 else "Tráfico normal"
    
    return {
        "codigo_prediccion": int(prediccion[0]),
        "diagnostico": estado
    }