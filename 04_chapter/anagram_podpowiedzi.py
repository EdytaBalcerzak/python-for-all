#gra w wymieszane litery
#komputer losuje slowo, a nastepnie miesza w nim litery
#gracz ma za zadanie odgadnąć słowo

import random
WYRAZ = ("basen", "flądra", "niebanalny", "framuga", "kłopot", "dzieło")
wyraz = random.choice(WYRAZ)
# print(wyraz)
prawidłowy = wyraz

wymieszany = ""
while wyraz:
    losowa_litera = random.randrange(len(wyraz))
    # print(losowa_litera)
    wymieszany += wyraz[losowa_litera]
    # print(wymieszany)
    wyraz = wyraz[:losowa_litera] + wyraz[(losowa_litera + 1):]
    # print(wyraz)

print("Witaj w grze WYMIESZANE LITERY")
print("Postaraj się odgadnąć co to za słowo\n\n\n")
print(wymieszany)
punkty = 0
opcja = input("Potrzebujesz podpowiedzi? Tak, czy nie?")
if opcja == "tak":
    print("drugą literą w tym wyrazie jest:", prawidłowy[1], ", czwarta litera to: ", prawidłowy[3])
    punkty += 1
    odpowiedz = input("\nWpisz odpowiedź:")
else:
    odpowiedz = input("\nWpisz odpowiedź:")
    punkty += 2
while odpowiedz != prawidłowy and odpowiedz!= "":
    print("Niestety, nie zgadłeś, spróbuj jeszcze raz")

if odpowiedz == prawidłowy:
    print("brawo, zgadłeś")
    print("Łączna ilość punktów: ", punkty)


wyraz = random.choice(WYRAZ)
prawidłowy = wyraz

wymieszany = ""
while wyraz:
    losowa_litera = random.randrange(len(wyraz))
    wymieszany += wyraz[losowa_litera]
    wyraz = wyraz[:losowa_litera] + wyraz[(losowa_litera + 1):]
print(wymieszany)

opcja = input("Potrzebujesz podpowiedzi? Tak, czy nie?")
if opcja == "tak":
    print("drugą literą w tym wyrazie jest:", prawidłowy[1], ", czwarta litera to: ", prawidłowy[3])
    punkty += 1
    odpowiedz = input("\nWpisz odpowiedź:")
else:
    odpowiedz = input("\nWpisz odpowiedź:")
    punkty += 2
while odpowiedz != prawidłowy and odpowiedz!= "":
    print("Niestety, nie zgadłeś, spróbuj jeszcze raz")

if odpowiedz == prawidłowy:
    print("brawo, zgadłeś")
    print("\n\nLączna ilość punktów: ", punkty)


wyraz = random.choice(WYRAZ)
prawidłowy = wyraz

wymieszany = ""
while wyraz:
    losowa_litera = random.randrange(len(wyraz))
    wymieszany += wyraz[losowa_litera]
    wyraz = wyraz[:losowa_litera] + wyraz[(losowa_litera + 1):]
print(wymieszany)

opcja = input("Potrzebujesz podpowiedzi? Tak, czy nie?")
if opcja == "tak":
    print("drugą literą w tym wyrazie jest:", prawidłowy[1], ", czwarta litera to: ", prawidłowy[3])
    punkty += 1
    odpowiedz = input("\nWpisz odpowiedź:")
else:
    odpowiedz = input("\nWpisz odpowiedź:")
    punkty += 2
while odpowiedz != prawidłowy and odpowiedz!= "":
    print("Niestety, nie zgadłeś, spróbuj jeszcze raz")

if odpowiedz == prawidłowy:
    print("brawo, zgadłeś")
    print("\n\nLączna ilość punktów: ", punkty)


wyraz = random.choice(WYRAZ)
prawidłowy = wyraz

wymieszany = ""
while wyraz:
    losowa_litera = random.randrange(len(wyraz))
    wymieszany += wyraz[losowa_litera]
    wyraz = wyraz[:losowa_litera] + wyraz[(losowa_litera + 1):]
print(wymieszany)

opcja = input("Potrzebujesz podpowiedzi? Tak, czy nie?")
if opcja == "tak":
    print("drugą literą w tym wyrazie jest:", prawidłowy[1], ", czwarta litera to: ", prawidłowy[3])
    punkty += 1
    odpowiedz = input("\nWpisz odpowiedź:")
else:
    odpowiedz = input("\nWpisz odpowiedź:")
    punkty += 2
while odpowiedz != prawidłowy and odpowiedz!= "":
    print("Niestety, nie zgadłeś, spróbuj jeszcze raz")

if odpowiedz == prawidłowy:
    print("brawo, zgadłeś")
    print("\n\nLączna ilość punktów: ", punkty)



input("Aby zakończyć program, naciśnij Enter")
