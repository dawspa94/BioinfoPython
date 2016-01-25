Dawid:
#BioinfoPython

def wpisz():
    imie = input("Podaj imie: ")
    ocena = input("Podaj ocene: ")
    if imie in dziennik:
        dziennik[imie].append(float(ocena))
        print("Dodano ocene")
    else:
        print("Taka osoba nie istnieje")
def wpisz2():
    for imie in dziennik:
        lista = dziennik[imie]
        srednia = mean(lista)
        print(imie+ +srednia)
dziennik = {'Jan': [2, 3, 4, 5],
            'Patryk': [2, 3, 4, 5],
            'Edek': [2, 3, 4, 5],
            'Marian': [2, 3, 4, 5]
           }
def menu():
    print("""
        Dzienniczek ver 1.0

        Witaj w menu:
        [1] Wpisz ocene
        [2] Ocena na zaliczenie
        [3] Usun wpis
        [4] Wyjscie""")
    a = input("Twoj wybor: ")
    if a == "1":
        wpisz()
    elif a == "2":
        wpisz2()
    elif a =="3":
        print ("usuń wpis")
    elif a == "4":
        exit()
    else:
        print("Nie ma takiej opcji")
while True:
    menu()
