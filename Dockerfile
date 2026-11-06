# Usar una imagen oficial y ligera de Python
FROM python:3.12-slim

# Establecer la carpeta de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de requerimientos e instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar solo el código de la API y la carpeta del modelo entrenado
COPY main.py .
COPY mlruns/ ./mlruns/

# Exponer el puerto por donde escuchará FastAPI
EXPOSE 8000

# Comando para encender el servidor automáticamente
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]