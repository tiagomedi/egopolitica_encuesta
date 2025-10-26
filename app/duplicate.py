import pandas as pd
df = pd.read_csv("./data/NEW_CSV_TOTAL.csv")
df = df.drop_duplicates(subset="Id_Encuesta")

df.to_csv("./media/Encuestado_sin_duplicados.csv", index=False)