#!/usr/bin/python
# -*- coding: utf-8 -*-

#Utwórz program, który wypisuje listę słów w przypadkowej kolejności.
#Program powinien wypisać wszystkie słowa bez żadnych powtórzeń.
import random
slowa = ["cukierek", "bocian", "miś", "agrafka", "łóżko", "kabaret"]
kopia_slowa = slowa[:]


haslo = random.choice(kopia_slowa)
wyraz = haslo
while kopia_slowa:
    print(haslo)

    if haslo in kopia_slowa:
        kopia_slowa.remove(haslo)
    if kopia_slowa:
        haslo = random.choice(kopia_slowa)

input("Aby zakonczyc, nacisnij Enter")
