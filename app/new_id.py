import pandas as pd

df = pd.read_csv("./data/NEW_CSV_TOTAL.csv")

if 'Id_Encuesta' not in df.columns:
    raise ValueError("❌ No se encontró la columna 'Id_Encuesta' en el CSV.")

df['Id_Encuesta'] = range(1, len(df) + 1)

df.to_csv("./data/NEW_CSV_TOTAL_REHACIDO.csv", index=False, encoding='utf-8-sig')

print("✅ Archivo generado correctamente: ./media/NEW_CSV_TOTAL_REHACIDO.csv")
print(f"Total de filas procesadas: {len(df)}")
