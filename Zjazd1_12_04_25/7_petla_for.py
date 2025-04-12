napis = input('Napisz cos:   ')
licznik_a = 0
licznik_spacja = 0
licznik_kropka = 0
for i in range(len(napis)):
    # print(napis[i])
    if napis[i] == 'a':
        print(f'znaleziono litre a na pozycji {i}')
#        licznik_a = licznik_a + 1
        licznik_a += 1
    if napis[i] == ' ':
        print(f'znaleziono spacje na pozycji {i}')
        licznik_spacja = licznik_spacja + 1
    if napis[i] == '.':
        print(f'znaleziono . na pozycji {i}')
        licznik_kropka = licznik_kropka + 1

print(f'Litera a wystapiła {licznik_a} razy')
print(f'Znaleniono {licznik_spacja+1} slow')
print(f'Znaleniono {licznik_kropka} zdan')

# wypiszmy statystyki - liczba slow, liczba zdań
