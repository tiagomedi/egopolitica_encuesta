import pandas as pd
import os

# Cargar el CSV
df = pd.read_csv("./data/Descripción_CSV.csv")

# Crear carpeta de salida
carpeta_salida = "./data_check/Tablas_respuestas"
os.makedirs(carpeta_salida, exist_ok=True)

# Agrupar por columna 'Pregunta'
for pregunta, grupo in df.groupby("Pregunta"):
    # Crear nombre de archivo (sin caracteres raros)
    nombre_archivo = f"{pregunta}.csv".replace("/", "_").replace("\\", "_")
    ruta_archivo = os.path.join(carpeta_salida, nombre_archivo)

    # Guardar solo las columnas relevantes
    grupo[["Pregunta","Codigo", "Descripcion"]].to_csv(ruta_archivo, index=False, encoding="utf-8-sig")
    print(f"✅ Archivo creado: {ruta_archivo}")

print("\nTodos los archivos fueron generados exitosamente.")
