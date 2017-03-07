#!/usr/bin/python
# -*- coding: utf-8 -*-

#algorytm z pseudokodem oraz aplikacja "Komputer zgaduje liczby"



#odpowiedz na pytanie komputera
#nastepnie wybierz liczbe w zakresie od 1 do 100
#komputer sprobuje odgadnac ja
#jesli liczba wybrana przez komputer bedzie zbyt mala lub za wielka, powiedz mu o tym
#jesli odgadnie, pogratuluj mu oraz powiedz ile prob mu to zajelo

print("pobawmy sie tak, ze wybierzesz jakas liczbe a ja postaram sie ja odgadnac")
zgoda = input("napisz ok , jesli sie zgadzasz \n")
print("\n\nZaczynajmy! Obstawiam liczbę: \n")

dolny_wynik = 1
gorny_wynik = 100
tries = 0


import random
liczba_komputera = random.randint(dolny_wynik, gorny_wynik)
print(liczba_komputera)

wynik = ""
while wynik != "ok":
    if wynik == "mniej":
        gorny_wynik = liczba_komputera - 1
        liczba_komputera = random.randint(dolny_wynik, gorny_wynik)
        print(liczba_komputera)
    elif wynik == "wiecej":
        dolny_wynik = liczba_komputera + 1
        liczba_komputera = random.randint(dolny_wynik, gorny_wynik)
        print(liczba_komputera)
    tries += 1
    wynik = input("powiedz mi czy jest 'ok', 'mniej' czy moze 'wiecej' \n")
print("\n\n\nJestem genialny. Udalo mi sie!!!", "Zajelo mi to tylko", tries, "prob")

input("\n\n\n\nAby zakonczyc program, nacisnij Enter")
