import pandas as pd

df = pd.read_csv('C:\\Users\\vdi-student\\Desktop\\Analiza_Danych_AI_2\\Zjazd1_12_04_25\\diabetes.csv')
print(df)
print(df.head(3).to_string())
print(f'Kształt DANYCH: {df.shape}')
print(df.describe().T.round(2).to_string())
