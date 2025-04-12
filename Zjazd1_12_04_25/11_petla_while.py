uzytkownicy = ['Kamil', 'Oliwia', 'Magda123', 'Kubus', 'Agata']
licznik = 0
nazwa = input('Podaj nazwe uzytkownika:   ')
while nazwa not in uzytkownicy:
    licznik += 1
    print(f'Próba {licznik} Źle, jeszcze raz')
    nazwa = input('Podaj nazwe uzytkownika:   ')

print(f'udalo sie za proba {licznik + 1}')
print(f'Siema {nazwa}')
