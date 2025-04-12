imie = input('Jak masz na imie?   ')
wiek = int(input('Ile masz lat?   '))
if wiek < 0:
    print('zly wiek')
elif wiek < 18:
    print(f'Siema {imie}, masz {wiek} lat')
    print(f'Bedziesz dorosly za {18 - wiek} lat')
elif wiek == 18:
    print('Mlody dorosly')
else:
    print('jestes dorosly')
