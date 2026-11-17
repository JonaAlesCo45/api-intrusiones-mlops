import streamlit as st
import requests
import random
import time

# Configuración básica de la página
st.set_page_config(page_title="Monitor IDS", page_icon="🛡️", layout="centered")

st.title("🛡️ Monitor de Intrusiones de Red")
st.markdown("Interfaz gráfica conectada al contenedor de Machine Learning.")

st.divider()

# URL de la API que está dentro de tu contenedor Docker
API_URL = "http://localhost:8000/predecir"

st.subheader("Simulador de Tráfico")
st.write("Haz clic en los botones para enviar datos al modelo y ver su reacción en vivo.")

# Botón 1: Simular tráfico normal (los 78 ceros de tu prueba)
if st.button("🟢 Enviar Tráfico Normal"):
    paquete_normal = [0.0] * 78  # 78 características en cero
    
    with st.spinner("Analizando paquete en la API..."):
        time.sleep(0.5) # Pequeña pausa para efecto visual
        try:
            # Enviamos el paquete a FastAPI
            respuesta = requests.post(API_URL, json={"caracteristicas": paquete_normal})
            datos = respuesta.json()
            
            # Mostramos el resultado con colores
            if datos["codigo_prediccion"] == 1:
                st.error(f"🔴 ¡ALERTA! {datos['diagnostico']}")
            else:
                st.success(f"✅ Análisis completado: {datos['diagnostico']}")
                
        except Exception as e:
            st.warning("⚠️ Error de conexión: ¿Seguro que el contenedor Docker está encendido?")

# Botón 2: Simular un ataque (números aleatorios altos)
if st.button("🔴 Simular Ataque de Red"):
    # Generamos 78 números altos/aleatorios para que el modelo lo detecte como anomalía
    paquete_ataque = [80.0, 1293792.0, 3.0, 7.0, 26.0, 11607.0, 20.0, 0.0, 8.666666667, 10.26320288, 5840.0, 0.0, 1658.142857, 2137.29708, 8991.398927, 7.72921768, 143754.6667, 430865.8067, 1292730.0, 2.0, 747.0, 373.5, 523.9661249, 744.0, 3.0, 1293746.0, 215624.3333, 527671.9348, 1292730.0, 2.0, 0.0, 0.0, 0.0, 0.0, 72.0, 152.0, 2.318765304, 5.410452376, 0.0, 5840.0, 1057.545455, 1853.437529, 3435230.673, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 2.0, 1163.3, 8.666666667, 1658.142857, 72.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 26.0, 7.0, 11607.0, 8192.0, 229.0, 2.0, 20.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    
    with st.spinner("Analizando paquete en la API..."):
        time.sleep(0.5)
        try:
            respuesta = requests.post(API_URL, json={"caracteristicas": paquete_ataque})
            datos = respuesta.json()
            
            if datos["codigo_prediccion"] == 1:
                st.error(f"🚨 ¡INTRUSIÓN BLOQUEADA! {datos['diagnostico']}")
            else:
                st.success(f"✅ Análisis completado: {datos['diagnostico']}")
                
        except Exception as e:
            st.warning("⚠️ Error de conexión: ¿Seguro que el contenedor Docker está encendido?")