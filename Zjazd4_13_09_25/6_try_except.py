# program pyta ile masz lat i mowi, kiedy bedziesz pelnoletni

while True:
    try:
        age = int(input('Ile masz lat?   '))
        break
    except ValueError:
        print('Zły wiek, Wprowadź jeszcze raz')


if age < 18:
    print(f'Będziesz dorosły za {18 - age} lat')
else:
    print('Jesteś dorosły')