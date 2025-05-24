import matplotlib.pyplot as plt

wydatki = ['mieszkanie', 'pies', 'rozrywka', 'pokemony', 'jedzenie']
wartosci = [2500, 4000, 50, 4000, 350]
explode = [0 for i in wydatki]
explode[3] = 0.1
explode[1] = 0.3
plt.pie(wartosci, labels=wydatki, explode=explode, shadow=True)
plt.show()
