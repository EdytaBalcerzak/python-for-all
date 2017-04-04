#!/usr/bin/python
# -*- coding: utf-8 -*-

#korzystanie z metod listy
#Program do tworzenia i utrzymywania listy najlepszych wynikow uzyskanych w grze komputerowej
wyniki = []
wybor = None

while wybor != 0:
    print(
    """
    Najlepsze wyniki
    0 - zakończ
    1 - pokaż wyniki
    2 - dodaj wynik
    3 - usuń wynik
    4 - posortuj wyniki
    """
    )
    wybor = int(input("Co wybierasz?"))
    if wybor == 0:
        print("Do zobaczenia")

    elif wybor == 1:
       print("Najlepsze wyniki:")
       for wynik in wyniki:
           print(wynik)
    #dodawanie wyniku
    elif wybor == 2:
       wynik_gracza = int(input("Podaj swój wynik: "))
       wyniki.append(wynik_gracza)
    #usuwanie wyniku
    elif wybor == 3:
        wynik_gracza = int(input("Który wynik usunąć? "))
        if wynik_gracza in wyniki:
            wyniki.remove(wynik_gracza)
        else:
            print("Nie ma takiego wyniku na liscie")
    #sortowanie wynikow
    elif wybor == 4:
        wyniki.sort(reverse=True)





input("Aby zakończyć program, naciśnij Enter")
