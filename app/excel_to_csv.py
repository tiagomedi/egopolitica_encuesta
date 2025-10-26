import pandas as pd

xlsx = pd.read_excel('./data/Descripción.xlsx', sheet_name=None)

combined = pd.concat(xlsx.values(), ignore_index=True)

combined.to_csv('new_excel.csv', index=False)
    