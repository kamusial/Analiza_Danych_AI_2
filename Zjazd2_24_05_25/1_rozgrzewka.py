# przyjmie nazwe pliku (zabezpieczenia)
# przyjmie rozszerzenie
# powie, czy rozszerzenie dozwolone - jeśli nie, to podaj inne
# program napisze ładnie nazwe z rozszerzeniem
# program wykona to dla X plików danych razem

extentions = ['txt', 'csv', 'jpg', 'mp3']

file_names = input('podaj nazwy:  ').split()
for file_name in file_names:
    #file_name = input('Podaj nazwe pliku:   ')
    print(f'Podana nazwa {file_name} \na 2 + 2 to {2+2}')
    # len(x)

    counter_a = 0
    while True:
        ext_name = input('Podaj rozszerzenie:   ')
        if ext_name in extentions:
            print(f'zaakceptowano {ext_name}')
            break
        else:
            print('niepoprawne rozszerzenie')
            #counter_a = counter_a + 1
            counter_a += 1
            if counter_a == 3:
                decission = input('czy przyjac txt? t/n ')
                if decission == 't':
                    ext_name = 'txt'
                    break
                else:
                    quit()

full_file_name = file_name+'.'+ext_name
print(full_file_name)



