name = input('Podaj nazwe:    ')
haslo = input('Podaj haslo:   ')

while True:
    if name == 'Piesek' and haslo == '1234':
        break
    elif name == '' and haslo == 'serwis':
        haslo2 = int(input('haslo2:   '))
        if haslo2 == 1000:
            break
    elif name == 'exit':
        quit()
print('Witamy w programie')
