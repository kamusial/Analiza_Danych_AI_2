import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv("otodom.csv")

print(df.describe().T.round(2).to_string())


print(df.to_string())
# print(df.iloc[7:15, 1:4])  # wytnij wiersze i kolumny

sns.heatmap(df.iloc[:,1:].corr(), annot=True)
plt.show()