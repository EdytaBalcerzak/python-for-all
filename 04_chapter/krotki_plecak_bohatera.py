#program ukazujacy dzizalanie krotek
#pokazuje plecak bohatera gry

plecak = ()
if not plecak:
    print("Masz puste ręce")
input("Aby kontynuować, nacisnij Enter")

plecak = ("miecz", "zbroja", "tarcza", "dezodorant")
print("\n\nWykaz zawartości plecaka (krotki)")
print(plecak)
print("\nElementy Twojego wyposażenia:")
for rzeczy in plecak:
    print(rzeczy)
input("\nAby kontynuować, nacisnij Enter")

#liczę dlugość krotki
objetosc = len(plecak)
print("\n\nTwoj dobytek zawiera", objetosc, "elementy")
input("\nAby kontynuować, nacisnij Enter")

#sprawdzam czy element nalezy do krotki
if "dezodorant" in plecak:
    print("\n\nDozyjesz dnia w ktorym stoczysz walkę")

indeks = int(input("Wprowadż indeks elementu inwentarza: "))
print("\n\nPod indeksem", indeks, "znajduje się", plecak[indeks])
poczatek_indeksu = int(input("Wprowadź indeks wyznaczający początek wycinka: "))
koniec_indeksu = int(input("Wprowadź indeks wyznaczający koniec wycinka: "))
print("wyposażenie[", poczatek_indeksu, ":", koniec_indeksu, "]", end= " ")
print(plecak[poczatek_indeksu:koniec_indeksu])
input("\nAby kontynuować, nacisnij Enter")
inne = ("złoto", "papierosy")
print("\n\n\nZnajdujesz skrzynię, która zawiera:")
print(inne)
print("\nDodajesz zawartość skrzyni do swojego inwentarza.")
plecak += inne
print("\nTwój aktualny inwentarz to:")
print(plecak)
input("\n\n\naby zakonczyc gre, nacisnij Enter")
