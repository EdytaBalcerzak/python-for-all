#program wybiera losowo pozycje w lancuchu
#prezentuje dostep swobodny do elementu sekwencji

slowo = "kalkulator"
import random
print("Losowe indeksowanie lancucha znakow")
print("\n\nWartosc zmiennej slowo to: ", slowo, "\n\n")
wysoko = len(slowo)
nisko = -len(slowo)

for i in range(10):
    pozycja = random.randrange(wysoko, nisko)
    print("word[", pozycja, "] :", slowo[pozycja])
input("Aby zakonczyc program , nacisnij Enter")
