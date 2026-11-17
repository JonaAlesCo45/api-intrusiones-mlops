import pandas as pd

print("Cargando dataset...")
df = pd.read_csv('data/Clean_CICIDS2017.csv')

print(f"\nTotal de filas: {len(df)}")
print(f"Total de columnas: {len(df.columns)}")

# La columna de la etiqueta siempre debe ser la última
col_etiqueta = df.columns[-1]
print(f"\nLa columna de etiqueta parece llamarse: '{col_etiqueta}'")

# Veamos qué valores únicos tiene esa columna
valores_unicos = df[col_etiqueta].unique()
print(f"Valores únicos en esa columna: {valores_unicos}")

# Asumiendo que 0 es normal, cualquier otro valor es un ataque
ataques = df[df[col_etiqueta] != 0.0]

if not ataques.empty:
    print(f"\n¡Se encontraron {len(ataques)} ataques!")
    # Tomar el primer ataque y extraer sus 78 características
    caracteristicas = ataques.iloc[0, :-1].tolist()
    print("\n--- COPIA LA LISTA DE ABAJO PARA EL FRONTEND ---")
    print(caracteristicas)
else:
    print("\nDefinitivamente no hay ataques. El dataset parece contener solo tráfico normal (0).")