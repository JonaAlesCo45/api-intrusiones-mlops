import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, recall_score
import mlflow
import mlflow.sklearn

# 1. Cargar los datos
print("Cargando la muestra de datos...")
df = pd.read_csv("data/muestra_cicids.csv")

# Limpieza rápida: usar solo columnas numéricas y rellenar vacíos
df = df.fillna(0)
X = df.iloc[:, :-1].select_dtypes(include=['float64', 'int64']) # Características del paquete de red
y = df.iloc[:, -1] # La etiqueta (Normal o Ataque)

# Convertir etiquetas a binario (0 = Normal, 1 = Ataque)
# Nota: En CICIDS2017 el tráfico normal se llama 'BENIGN'
y_binario = y.apply(lambda x: 0 if x == 'BENIGN' else 1)

X_train, X_test, y_train, y_test = train_test_split(X, y_binario, test_size=0.2, random_state=42)

# 2. Configurar MLflow y Entrenar
mlflow.set_experiment("Deteccion_Intrusiones_Red")

with mlflow.start_run():
    arboles = 50
    profundidad = 10
    
    print("Entrenando el algoritmo Random Forest...")
    modelo = RandomForestClassifier(n_estimators=arboles, max_depth=profundidad, random_state=42)
    modelo.fit(X_train, y_train)

    print("Evaluando el modelo...")
    predicciones = modelo.predict(X_test)
    precision = accuracy_score(y_test, predicciones)
    recall = recall_score(y_test, predicciones) # El Recall es vital en ciberseguridad para no ignorar ataques reales

    # 3. Registrar métricas y guardar el modelo automáticamente
    mlflow.log_param("n_estimators", arboles)
    mlflow.log_param("max_depth", profundidad)
    mlflow.log_metric("accuracy", precision)
    mlflow.log_metric("recall", recall)
    
    mlflow.sklearn.log_model(modelo, "modelo_rf", skops_trusted_types=["sklearn.tree._tree.Tree"])

    print(f"¡Entrenamiento finalizado y registrado! Precisión: {precision:.4f}, Recall: {recall:.4f}")