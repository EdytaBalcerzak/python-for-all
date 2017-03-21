#referencje współdzielone
chlopak = ["wysoki", "szczupły", "inteligentny"]
michal = chlopak
kochanie = chlopak
hasan = chlopak

print(kochanie)
#wyciecie oraz przypisanie do zmiennej "kochanie , kopii listy michal"
kochanie = michal[:]

kochanie[1] = "gruby"
print(kochanie)

print(michal)
print(hasan)

input("Aby zakonczyc program , nacisnij Enter")
