name = input('Podaj nazwe:    ')
haslo = input('Podaj haslo:   ')

while name != 'Piesek' or haslo != '1234':
    print('Zly user albo haslo')
    name = input('Podaj nazwe')
    haslo = input('Podaj haslo')

print('Witamy w systemie')