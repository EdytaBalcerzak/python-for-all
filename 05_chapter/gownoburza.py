#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
wybor = None
ojcowie = ["Tom Cruise ", "Ferdynand Kiepski", "Donald Tusk", "Krzysztof Ibisz",
"Jozef Pilsudzki", "Antoni Macierewicz", "Adam Mickiewicz", "Henryk Sienkiewicz"]
rodzina = {}
while wybor != 0:
    print("""
    0 - wyjdz
    1 - sprawdz, kto jest jego ojcem
    2 - sprawdz, kto jest jego dziadkiem
    3 - dodaj parę syn-ojciec
    4 - usuń parę syn-ojciec
    5 - lista wszystkich ojcow
    """)
    wybor = input("Wybór: ")
    if len(rodzina) == 0 and  wybor < 3 and wybor == 4:
        print("Najpierw dodaj parę syn-ojciec (3), a następnie skorzystaj z \n" +
            "pozostałych opcji")
        continue
    elif wybor == 0:
        print("Do zobaczenia")
    elif wybor == 1:
        syn = raw_input("Podaj imię i nazwisko osoby do sprawdzenia\n")
        print("\n\n", syn, ".Jego ojciec to ", rodzina[syn])
    elif wybor == 2:
        syn = raw_input("\nCzyjego dziadka chcesz poznać?\n")
        if syn in rodzina:
            ojciec = rodzina[syn]
            dziadek = rodzina[ojciec]
            print("\n\n", syn, " jego dziadek to ", dziadek)
    elif wybor == 3:
        nowy_syn = ""
        nowy_syn = raw_input("Podaj imię i nazwisko syna:\n")
        ojciec = random.choice(ojcowie)
        while ojciec == nowy_syn:
            ojciec = random.choice(ojcowie)
        rodzina[nowy_syn] = ojciec
        print(rodzina)
    elif wybor == 4:
        print(ojcowie)
        syn = ""
        syn = raw_input("Którego syna chcesz usunąć?")
        rodzina.pop(syn, None)
    elif wybor == 5:
        print(ojcowie)


input("Aby zakonczyc, nacisnij Enter")
