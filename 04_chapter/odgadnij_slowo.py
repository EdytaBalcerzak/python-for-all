#komputer losowo wybiera słowo
#gracz stara sie je odgadnąć
#program informuje użytkownika ile liter zawiera słowo
#komputer pozwala na zadanie 5 pytań naprowadzających, na które odpowiada tylko 'tak' lub 'nie'
#gracz stara sie odgadnac haslo
#jesli mu sie uda, program gratuluje graczowi
#jesli nie, pozwala odpowiedziec jeszcze raz

import random
lista_hasel = ("lalka","lampa", "wiertło", "abażur", "miś")
slowo = random.choice(lista_hasel)
haslo = slowo
print("Witaj w grze 'Odgadnij Słowo'")
print("Jak się domyślasz, Twoim zadaniem będzie odgadnięcie hasła, wybranego losowo przez komputer.\n\nDo dzieła!")
print("\n\nHasło, które wybrałam, zawiera ", len(slowo), "słów")
print("\n\nMożesz zadać 5 pytań sprawdzających czy dana litera wchodzi w skład tego słowa")

litera_gracza = input("\n\nKtórą literę chcesz sprawdzić? ")
proba = 0
while True:
    if litera_gracza in haslo:
        print("\ntak , hasło zawierą tą literę")
    else:
        print("\nNie, ta litera nie występuje w haśle")
    proba += 1
    if proba == 5:
        break
    litera_gracza = input("Którą literę chcesz sprawdzić? ")
odpowiedz = input("podaj swoją odpowiedz\n")
if odpowiedz == haslo:
    print("\nJestes swietny, udało Ci się")
else:
    print("\nNiestety nie, dostaniesz jeszcze 3 kolejne podpowiedzi!")

    litera_gracza = input("\n\nKtórą literę chcesz sprawdzić? ")
    proba = 0
    while True:
        if litera_gracza in haslo:
            print("\ntak , hasło zawierą tą literę")
        else:
            print("\nNie, ta litera nie występuje w haśle")
        proba += 1
        if proba == 3:
            break
        litera_gracza = input("\n\nKtórą literę chcesz sprawdzić? ")
    odpowiedz = input("podaj swoją odpowiedz\n")
    if odpowiedz == haslo:
        print("\nJestes swietny, udało Ci się")
    else:
        print("\nNiestety nie.Przegrales")

input("Aby zakończyć grę, naciśnij Enter")
#litera_gracza = input("Którą literę chcesz sprawdzić?")
