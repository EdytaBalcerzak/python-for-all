print("\t\t\tProgram wyliczajcy faktyczna cene samochodu")
cena_samochodu = float(input("Podaj podstawowa cene samochodu"))
print("""Dodatkowe opaty:
        - podatek od kupna samochodu
        - oplata rejestracyjna
        - prowizja przygotowawcza dealera
        - oplata za dostarczenie
         """)
podatek = cena_samochodu * 0.02
rejestracja = cena_samochodu * 0.03
prowizja_dealer = 500
dostarczenie_oplata = 300

print("Laczna suma oplat za samochod:")

total = cena_samochodu + podatek + rejestracja + prowizja_dealer + dostarczenie_oplata

print(total)
input("aby zakonczyc program , nacisnij Enter")
    
