#!/usr/bin/python
# -*- coding: utf-8 -*-

#Utwórz program, który wypisuje listę słów w przypadkowej kolejności.
#Program powinien wypisać wszystkie słowa bez żadnych powtórzeń.
import random
slowa = ["cukierek", "bocian", "miś", "agrafka", "łóżko", "kabaret"]

for i in range(len(slowa)):
    print(i)
    haslo = random.choice(slowa)
    print(haslo)
    slowa.remove(haslo)

input("Aby zakonczyc, nacisnij Enter")
