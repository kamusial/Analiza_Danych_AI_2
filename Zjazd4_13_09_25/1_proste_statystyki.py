from statistics import mean, median, multimode

dane = [25, 27, 30, 30, 31, 33, 35, 35, 35, 36, 38, 40]

print(dane)
print(f'Element 6ty to {dane[5]}')
print('Lista ma',len(dane),'elementow')
print(f'Lista ma {len(dane)} elementow')
print(max(dane) / len(dane))

srednia = mean(dane)
mediana = median(dane)
moda = multimode(dane)

print(f'\nLiczba obserwacji: {len(dane)}')
print(f'Srednia: {round(srednia)}')  # zaokrąglona do całkowitej
print(f'Srednia: {round(srednia, 4)}') # zaokrąglona do 4 miejsc po przecinku
print(f'Srednia: {int(srednia)}') # zamiana na liczbe całkowitą
print(f'Srednia: {srednia:.2f}')
print(f'Mediana: {mediana}')
print(f'Moda: {moda}')

