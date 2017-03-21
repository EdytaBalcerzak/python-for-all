#dodawanie do listy zagniezdzonej krotki
#dostep do zagniezdzonych krotek


wyniki = []
wybor = None

while wybor != 0:
    print(
    """
    Najlepsze wyniki 2.0
    0 - zakończ
    1 - wyświetl wyniki
    2 - dodaj wynik
    """
    )
    wybor = int(input("Co wybierasz?"))
    if wybor == 0:
        print("Do zobaczenia")
    elif wybor == 1:
        print("\nLista Najlepszych Wyników")
        print("Gracz\tWynik")
        for lista in wyniki:
            wynik, imie = lista
            print(imie, "\t", wynik)
    elif wybor == 2:
        imie = input("Jak sie nazywasz?")
        wynik = int(input("Podaj swój wynik"))
        lista = (imie, wynik)
        wyniki.append(lista)
        wyniki.sort(reverse=True)
        wyniki = wyniki[:5]


input("Aby zakonczyć program, naciśnij Enter")
