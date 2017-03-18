#program wybiera losowo pozycje w lancuchu
#prezentuje dostep swobodny do elementu sekwencji

import random
slowo = "kwiat"
print("wartosc zmiennej 'slowo',to", slowo)
dodac = len(slowo)
odjac = -len(slowo)
for i in range(10):
    pozycja = random.randrange(odjac, dodac)
    print("slowo [", pozycja,"]\t", slowo[pozycja])
# print(slowo[4])
# print(slowo[2])
# print(slowo[-1])
# print(slowo[-5])

input("Aby zakonczyc , nacisnij Enter")
