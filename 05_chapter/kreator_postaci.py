# Napisz program Kreator postaci do gry z podziałem na role. Gracz powinien
# otrzymać pulę 30 punktów, którą może spożytkować na cztery atrybuty: siła,
# zdrowie, mądrość i zręczność. Gracz powinien mieć możliwość przeznaczania
# punktów z puli na dowolny atrybut, jak również możliwość odbierania
# punktów przypisanych do atrybutu i przekazywania ich z powrotem do puli.


print("Witaj w grze")
print("Za moment stoczysz walkę, przygotuj się do niej odpowiednio")
print("Masz do dyspozycji 4 atrybuty i 30 pkt do rozdzielenia na nie")
print("\nTwoje atrybuty to:\n")
atrybuty = {"sila": 0, "zdrowie": 0, "madrosc": 0, "zrecznosc": 0}
punkty = 30
for zdolnosci in atrybuty:
    print(zdolnosci)
print("\nIlość Twoich punktów: ", punkty)

wybor = None
wybor_atrybutu = ""
while wybor != 0:
    print(
    """
    0 - wyjdź z gry
    1 - dodaj punkty
    2 - usuń punkty
    3 - sprawdz stan punktów
    """
    )
    wybor = int(input("Co wybierasz? "))
    if wybor == 0:
        print("\nDo zobaczenia")
    elif wybor == 1:
        for lista in atrybuty:
            print(lista)
        if punkty > 0:
            wybor_atrybutu = input("\nW któym atrybucie chcesz zmienić punkty? ")
            if wybor_atrybutu in atrybuty:
                ilosc_punktow = int(input("\nPodaj ilość punktów , którą chcesz przyznać atrybutowi: "))
                punkty -= ilosc_punktow
                if punkty >= 0:
                    atrybuty[wybor_atrybutu] = ilosc_punktow
                else:
                    punkty += ilosc_punktow
                    print("\nMasz zbyt mala ilosc punktow")
        else:
            print("\nmasz zbyt małą ilość punktów")

    elif wybor == 2:
        if wybor_atrybutu in atrybuty:
            for lista in atrybuty:
                print(lista)
            wybor_atrybutu = input("\nZ którego atrybutu chcesz usunąć punkty? ")
            odjete_punkty = int(input("\nIle punktow chcesz odjac? "))
            if odjete_punkty > atrybuty[wybor_atrybutu]:
                print(wybor_atrybutu, " nie posiada tylu punktów")
            else:
                atrybuty[wybor_atrybutu] -= odjete_punkty
                punkty += odjete_punkty
        else:
            print("\natrybuty nie posiadają punktów")


    elif wybor == 3:
        print(atrybuty)
        print("\nilość dostępnych punktów ", punkty)


input("Aby zakonczyc grę, nacisnij Enter")
