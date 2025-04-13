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

sns.histplot(df.cena)
plt.savefig('plik.png')
plt.show()

plt.scatter(df.powierzchnia, df.cena)
plt.show()

sns.scatterplot(data=df, x='powierzchnia', y='cena')
plt.show()

X = df.iloc[:,2:]
y = df.cena

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
print(X_train)
