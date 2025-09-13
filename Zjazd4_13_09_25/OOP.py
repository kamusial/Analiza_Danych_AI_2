# auto1 = ['Toyota', 'Yaris', '2003', '32', 'Kamil Musial']
# auto1[2] = 2036
# print(auto1)

class Auto:
    def __init__(self, barwa, wiek):
        self.kolor = barwa
        self.stan = 5
        self.ilosc_paliwa = 10
        self.tryb_ekonomiczny = False
        self.spalanie_na_100 = 14
        self.rocznik = 2025 - wiek

    def zasieg(self):
        zasieg = self.ilosc_paliwa / self.spalanie_na_100 * 100 * 0.9
        return round(zasieg)

    def ustaw_tryb(self, tryb):
        if tryb == 'eco':
            self.tryb_ekonomiczny = True
            self.spalanie_na_100 = 10
            print('dodana informacja o pliku, godzina <....> zmiana trybu na eco')
        elif tryb == 'normal':
            self.tryb_ekonomiczny = False
            self.spalanie_na_100 = 14
            print('dodana informacja o pliku, godzina <....> zmiana trybu na eco')
        else:
            print('Bez zmian')


moje_bmw = Auto('black', 12)
print(moje_bmw.kolor)
print(moje_bmw.spalanie_na_100)

auto_Tomka = Auto('red', 2)
auto_Tomka.rocznik += 3

print(auto_Tomka.zasieg())
moje_bmw.ustaw_tryb('eco')
print(moje_bmw.tryb_ekonomiczny)
