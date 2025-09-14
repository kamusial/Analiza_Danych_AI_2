dane = [1, 2, 3, 4, 5]
y = 5

try:
    x = dane[5]
    x = x / y
except IndexError:
    print('nie znaleziono elementu')
    print('przyjmuję wartość 0')
    x = 0
except ZeroDivisionError:
    print('Nie dzielimy przez 0')
    print('przyjmuję wartość 1')
    x=1

print(f'Dalsza część programu, moja dana to: {x}')