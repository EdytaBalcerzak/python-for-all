#skonfigurowanie programu
#komputer loswo wybiera słowo
#gracz próbuje odgadnąć poszczególne jego litery
#jesli nie odgadnie słowa w porę, ludzik zostaje powieszony
print("Witaj w  grze SZUBIENICA\n")
print("\nWybiorę dla Ciebie słowo, a Ty postaraj się je odgadnąć, litera po literze")
print("Jeśli nie uda Ci sie tego zrobić w wyznaczonej ilości prób ,\n Twój ludzik zginie")
print("Zaczynamy!\n\n")
import random
LUDZIK = (
"""
------
|   |
|
|
|
|
|
|
|
----------
""",
"""
------
|   |
|   O
|
|
|
|
|
|
----------
""",
"""
------
|   |
|   O
|  -+-
|
|
|
|
|
----------
""",
"""
------
|   |
|   O
| /-+-
|
|
|
|
|
----------
""",
"""
------
|   |
|   O
| /-+-/
|
|
|
|
|
----------
""",
"""
------
|   |
|   O
| /-+-/
|   |
|
|
|
|
----------
""",
"""
------
|   |
|   O
| /-+-/
|   |
|   |
|   |
|   |
|
----------
""",
"""
------
|   |
|   O
| /-+-/
|   |
|   |
|  | |
|  | |
|
----------
""")
MAX_PROB = len(LUDZIK) - 1
HASLA = ("KRECIK", "JOGURT", "KOSTKA", "MONETA", "PIWO")

#innicjalizacja zmiennych
haslo = random.choice(HASLA)
proba = 0
odgadywane_haslo = "-" * len(haslo)
uzyte_litery = []

while proba < MAX_PROB and odgadywane_haslo != haslo:
    print(LUDZIK[proba])
    print("Wykorzystałeś już następujące litery\n", uzyte_litery)
    print("\nNarazie zagadkowe słowo wygląda tak:\n", odgadywane_haslo)


    litera = input("\nWprowadż literę: ")
    litera = litera.upper()
    if litera in uzyte_litery:
        print("\n\nTej litery juz uzyles, podaj inną")
        litera = input("\nWprowadż literę: ")
        litera = litera.upper()
    else:
        uzyte_litery.append(litera)
    if litera in haslo:
        print("\n\nTak. Ta litera występuje w wyrazie")
        nowe = ""
        for i in range(len(haslo)):
            if litera == haslo[i]:
                nowe += litera
            else:
                nowe += odgadywane_haslo[i]
        odgadywane_haslo = nowe
    else:
        print("\n\nNie , ta litera nie występuje w wyrazie")
        proba += 1
if proba == MAX_PROB:
    print(LUDZIK[proba])
    print("Nie udało Ci się, Twój ludzik został powieszony")
else:
    print("Udało Ci się , zgadłeś!")


input("Aby zakończyć grę, naciśnij Enter")
