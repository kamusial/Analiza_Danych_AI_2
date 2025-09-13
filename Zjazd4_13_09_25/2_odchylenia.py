import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.lines import lineStyles

kroki = np.array([6420, 7120, 10350, 9800, 12010, 4500, 5300, 7000, 8900, 15400, 7600, 8100, 30000, 7800])

print(f'typ: {type(kroki)}')

srednia = kroki.mean()
mediana = np.median(kroki)
min_v, max_v = kroki.min(), kroki.max()
rozstep = max_v - min_v

wariancja = np.var(kroki, ddof=1)
print(wariancja)
odchylenie = np.sqrt(wariancja)
print(odchylenie)

q1, q3 = np.percentile(kroki, [25, 75])
iqr = q3 - q1  # rozpiętosc srodkowych 50% danych

print(q1, q3, iqr)

# rozrzut
rozrzut = odchylenie / srednia
print(f'wspolczynnik zmiennosci: {rozrzut}')

# reguła Tukeya
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr
odpady = kroki[(kroki < lower) | (kroki > upper)]
print(odpady)


# histogram
plt.figure(figsize=(7,4))
plt.hist(kroki, bins=10)
plt.axvline(srednia, linestyle='--', linewidth=2, label=f'średnia = {srednia:.0f}')
plt.axvline(mediana, linestyle=':', linewidth=2, label=f'mediana = {mediana:.0f}')
plt.title('Histogram dziennej liczny kroków')
plt.xlabel('Kroki')
plt.ylabel('Liczba')
# plt.legend()
plt.show()

# boxplot
plt.figure(figsize=(6, 4))
plt.boxplot(kroki, vert=True, showmeans=True)
plt.title('Boxplot')
plt.ylabel('Kroki')
plt.tight_layout()
plt.show()