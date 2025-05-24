# przyjmie nazwe pliku (zabezpieczenia)
# przyjmie rozszerzenie
# powie, czy rozszerzenie dozwolone - jeśli nie, to podaj inne
# program napisze ładnie nazwe z rozszerzeniem
# program wykona to dla X plików danych razem

extentions = ['txt', 'csv', 'jpg', 'mp3']

file_name = input('Podaj nazwe pliku:   ')
print(f'Podana nazwa {file_name} \na 2 + 2 to {2+2}')
# len(x)

ext_name = input('Podaj rozszerzenie:   ')
if ext_name in extentions:
    print(f'zaakceptowano {ext_name}')
else:
    print('niepoprawne rozszerzenie')

