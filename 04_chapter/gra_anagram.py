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
odpowiedz = input("\nWpisz odpowiedź:")
while odpowiedz != prawidłowy and odpowiedz!= "":
    print("Niestety, nie zgadłeś, spróbuj jeszcze raz")
    odpowiedz = input("\nWpisz odpowiedź:")

if odpowiedz == prawidłowy:
    print("brawo, zgadłeś")


input("Aby zakonczyć grę, nacisnij Enter")
