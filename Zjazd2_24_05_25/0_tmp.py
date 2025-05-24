file_names = input('podaj nazwy:  ').split()
print(file_names)

import pandas as pd
import numpy as np

df = pd.read_csv('C:\\Users\\vdi-student\\Desktop\\Analiza_Danych_AI_2\\Zjazd1_12_04_25\\diabetes.csv')
print(df)

#df.loc

print(df.iloc[  2:9 , 3:5   ])