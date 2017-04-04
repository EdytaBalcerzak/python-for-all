


#parametry z wartościami pozycyjnymi
def urodziny1(imie, wiek):
    print("Szczęśliwych urodzin,", imie, "!", " Masz już", wiek, "lat.\n")
# parametry z wartościami domyślnymi
def urodziny2(imie = "Edyta", wiek = 8):
    print("Szczęśliwych urodzin,", imie, "!", " Masz już", wiek, "lat.\n")

urodziny1("Edyta", 8)
urodziny1(8, "Edyta")
urodziny1(imie = "Edyta", wiek = 8)
urodziny1(wiek = 8, imie = "Edyta")

urodziny2()
urodziny2(imie = "Asia")
urodziny2(wiek = 10)
urodziny2(imie = "Asia", wiek = 10)
urodziny2("Asia", 10)
urodziny2()


input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
