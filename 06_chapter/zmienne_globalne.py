

def odczytywanie_globalnej():
    print("\n\nWartosc zmiennej numer odczytana wewnątrz zakresu lokalnego",
    "\nfunkcji oczytywanie_globalnej() wynosi: ", numer)

def przyslanianie_globalnej():
    numer = -10
    print("\n\nWartosc zmiennej numer odczytana wewnątrz zakresu lokalnego",
    "\nfunkcji przyslanianie_globalnej() wynosi: ", numer)

def zmiana_globalnej():
    global numer
    numer = -10
    print("\n\nWartosc zmiennej numer odczytana wewnątrz zakresu lokalnego",
    "\nfunkcji zmiana_globalnej() wynosi: ", numer)

numer = 10
print("W zakresie globalnym, wartość zmiennej numer została ustawiona na: ", numer)


#odczytywanie zmiennej globalnej wewnątrz funkcji
odczytywanie_globalnej()
print("Po powrocie do zakresu globalnego, wartość zmiennej numer",
"\nnadal wynosi", numer)

#przysłanianie zmiennej globalnej wewnątrz funkcji
przyslanianie_globalnej()
print("Po powrocie do zakresu globalnego, wartość zmiennej numer",
"\nnadal wynosi", numer)

#zmiana zmiennej globalnej wewnątrz funkcji
zmiana_globalnej()
print("Po powrocie do zakresu globalnego, wartość zmiennej numer",
"\nzmieniła się na", numer)

input("Aby zakonczyc , nacisnij Enter")
