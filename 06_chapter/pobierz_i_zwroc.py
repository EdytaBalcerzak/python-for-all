
#przypisanie parametrowi "wiadomosc" wartosci dostarczonej przez argument "To wiadomosc dla Ciebie"
def tekst(wiadomosc):
    print(wiadomosc)

def zwracanie():
    pięć = 5
    return pięć

def tak_czy_nie(pytanie):
    """Zadaj pytanie"""
    odpowiedz = None
    while odpowiedz not in ("tak", "nie"):
        odpowiedz = input(pytanie).lower()
    return odpowiedz

tekst("To wiadomosc dla Ciebie")
numer = zwracanie()
print("Oto co otrzymałam dzięki tej funkcji", numer)

odpowiedz = tak_czy_nie("Odpowiesz? Tak czy nie?")
print("Dzieki za wprowadzenie", odpowiedz)

input("Aby zakonczyc, nacisnij Enter")
