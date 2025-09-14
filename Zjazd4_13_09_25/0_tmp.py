import pandas as pd


slowo = 'kamil. dsd. asd .asd a.sd a.sdqwe.e .e. ..e . '
slowo = slowo.replace('.',',')
print(slowo)

liczba = 5

print(type(slowo))
print(type(liczba))

dane = [6420, 7120, 10350, 9800, 12010, 4500, 5300, 7000, 8900, 15400, 7600, 8100, 30000, 7800]

df = pd.DataFrame(dane)

df.describe()

lista_zakupow = ['marchew', 2, 'woda', 6, 'jajka', 12, 'woda', 2]
losta_zakupow2 = [
           ['marchew', 2],
          ['woda', 6],
          ['jajka', 12],
          ['woda', 2]
]


slownik_zakupow = {'marchew': 2, 'woda': 6, 'jajka': 12, 'woda': 2}
print(slownik_zakupow)
print(slownik_zakupow['jajka'])

dane = ['student', 'uczen', 'bezrobotny', 'pracujacy', 'bezrobotny_student']

for status in dane:
    print(f'typ czlowieka: {status}')
    if status == 'uczen' or status == 'student':
        print('ok')

cars = ['bmw', 'volvo','dacia', 'ford', 'citroen']
for car in cars:
    print(f'Sprawdzam, czy marka: {car} jest w bazie')


