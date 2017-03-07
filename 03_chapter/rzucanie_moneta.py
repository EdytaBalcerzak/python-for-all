#Program "Rzuć monetą"
#Program 100x rzuca monetą
#Następnie liczy ilość wyrzuconych "Reszek" i "Orzełków"

print("Rzuć monetą")
print("100 razy Rzucę monetą, a nastepnie podam ilość wyrzuconych Reszek i Orzelków ")
import random

orzelek = 0
reszka = 0
tries = 0
while tries != 100:
    rzut_moneta = random.randint(1, 2)
    if rzut_moneta == 1:
        orzelek += 1
    elif rzut_moneta == 2:
        reszka += 1
    tries += 1


print("\n\nIlosc wyrzuconych Reszek:", reszka)
print("\n\nIlosc wyrzuconych Orzelkow:", orzelek)

input("\n\n\n\n\nAby zakonczyc program, nacisnij Enter")
