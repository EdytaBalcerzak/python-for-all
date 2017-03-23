#tworzenie słowników
zargon = {
"Lifehack": "ogólna nazwa sposobów i trików używanych do ułatwiania" +
" sobie życia. W szczególności są to pomysły programistów, którzy próbują " +
"przenosić idee i koncepcje informatyczne na codzienne życie",

"Geek": " człowiek, który dąży do pogłębiania swojej wiedzy i umiejętności w " +
"jakiejś dziedzinie w stopniu daleko wykraczającym poza zwykłe hobby.",

"Meatware": "żartobliwe określenie użytkownika jako części systemu " +
"komputerowego,",

"Swapowanie": "potoczne lub żargonowe określenie sytuacji, w której komputer " +
"znacznie zwalnia pracę z powodu niedostatecznej ilości pamięci operacyjnej RAM"
}
# sprawdzanie przynaleznosci przed sprawdzaniem wartosci
if "Meatware" in zargon:
    print("znajduje sie")
#pobieranie wartosci ze słownika za pomocą metody get
print(zargon.get("Meatware", "metoda get do pobrania wartosci"))

wybor = None

print("Słownik slangu komputerowego/n")
print("""
0 - zakończ
1 - znajdź termin
2 - dodaj nowy termin
3 - zmień definicję terminu
4 - usuń termin
5 - lista terminów w słowniku
""")

while wybor != 0:
    wybor = int(input("\nCo wybierasz?\n\n"))
    if wybor == 0:
        print("Do zobaczenia")
    #pobranie wartości
    elif wybor == 1:
        termin = input("Jaki termin mam wyjaśnić?")
        if termin in zargon:
            definicja = zargon[termin]
            print(termin, "oznacza", definicja)
        else:
            print("Niestety, tego hasla nie ma w słowniku")
    #dodanie pary: klucz- wartosc
    elif wybor == 2:
        termin = input("Jaki termin chcesz dodać?")
        if termin not in zargon:
            definicja = input("Podaj wyjaśnienie terminu")
            zargon[termin] = definicja
        else:
            print("To hasło już znajduje się w słowniku")
    #wymiana pary: klucz- wartosc
    elif wybor == 3:
        termin = input("Definicję którego terminu chcesz zmienic?")
        if termin in zargon:
            definicja = input("Podaj nowe wyjaśnienie")
            zargon[termin] = definicja
        else:
            print("Nie ma takiego terminu w słowniku")
    #usunięcie pary: klucz - wartość
    elif wybor == 4:
        termin = input("Który termin w słowniku chcesz skasować?")
        if termin in zargon:
            del zargon[termin]
            print("Hasło usunięte")
        else:
            print("Nie ma takiego hasla w słowniku")
    #pokazanie wszystkich hasel w słowniku
    elif wybor == 5:
        # for terminy in zargon:
        #     print("\n", terminy)
        print(zargon.keys())
    else:
        print("Niestety,",  wybor, " to nieprawidłowy wybór")


input("Aby zakonczyc, nacisnij Enter")
