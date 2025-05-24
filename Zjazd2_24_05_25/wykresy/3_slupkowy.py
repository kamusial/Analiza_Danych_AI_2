import matplotlib.pyplot as plt
import random

names = ['Kamil', 'Kasia', 'Bartosz', 'Maja', 'piesek']
points = [random.randint(3, 15) for name in names]

plt.bar(names, points, color=['green', 'blue', 'yellow'])
plt.xticks(names)
plt.yticks(points)
plt.show()