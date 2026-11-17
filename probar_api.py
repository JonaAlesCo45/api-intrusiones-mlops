import requests

# Generamos una lista exacta de 78 características simuladas
datos_simulados = [0.0] * 78

url = "http://localhost:8000/predecir"
payload = {"caracteristicas": datos_simulados}

print("Enviando paquete de red a la API (78 características)...")

try:
    respuesta = requests.post(url, json=payload)
    print("Código de estado:", respuesta.status_code)
    print("Respuesta del modelo:", respuesta.json())
except requests.exceptions.ConnectionError:
    print("Error: No se pudo conectar. ¿Seguro que el contenedor Docker está corriendo?")