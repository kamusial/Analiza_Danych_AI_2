zakupy = ['marchew', 'woda', 'sok', 'mydlo', 'mleko']
print(zakupy)
print(zakupy[3])
print(zakupy[2:5])

for i in range(len(zakupy)):
    if len(zakupy[i]) > 4:
        print('Za dlugie')

imiona = ['Kamil', 'Agata', 'Iwona', 'Jakub', 'Tomasz', 'Kuba']
for i in range(len(imiona)):
    if imiona[i][-1] == 'a' and imiona[i] != 'Kuba':
        print(f'Szanowna Pani {imiona[i]}')
    else:
        print(f'Szanowny Pan {imiona[i]}')

for imie in imiona:
    if imie[-1] == 'a' and imie != 'Kuba':
        print(f'Szanowna Pani {imie}')
    else:
        print(f'Szanowny Pan {imie}')
