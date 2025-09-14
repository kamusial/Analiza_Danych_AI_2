import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('iris.csv')
print(df['class'].value_counts())

species = {
    'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica': 2
}
df['class_value'] = df['class'].map(species)
print(df.describe())

# plt.hist(df['sepallength'])
# plt.show()

# plt.scatter(df['sepallength'], df['sepalwidth'])
# plt.show()

sample = [5.6, 3.2, 5.2, 1.45]

sns.scatterplot(df, x='sepallength', y='sepalwidth', hue='class')
plt.scatter(5.6, 3.2, c='r')
plt.show()

sns.scatterplot(df, x='petallength', y='petalwidth', hue='class')
plt.scatter(5.2, 1.45, c='r')
plt.show()

# dystans między próbką, a istniejącymi danymi
df['distance'] = (df.sepallength - 5.6)**2 + (df.sepalwidth - 3.2)**2 + \
                 (df.petallength - 5.2)**2 + (df.petalwidth - 1.45)**2

print(df.head(5).to_string())
print(df.sort_values('distance').head(7).to_string())

print('Algorytm KNN')
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

X = df.iloc[:, :4]
y = df.class_value
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = KNeighborsClassifier(n_neighbors=5, weights='distance')
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
print(pd.DataFrame(confusion_matrix(y_test, model.predict(X_test))))

result = []
for k in range(1, 101):
    model = KNeighborsClassifier(n_neighbors=k, weights='distance')
    model.fit(X_train, y_train)
    result.append(model.score(X_test, y_test))
plt.plot(range(1, 101), result)
plt.show()