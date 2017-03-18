#wycinanie sekwencji

zdanie = "wykałaczka"
print("Podaj początkowy i koncowy indeks wycinka lancucha 'wykałaczka', a nastepnie zatwierdz go Enterem\n\n\n ")
poczatek = None
while poczatek != "":
    poczatek = (input("Poczatek "))
    if poczatek:
        poczatek = int(poczatek)
        koniec = int(input("Koniec "))
        print("word[", poczatek, ":", koniec, "], to: ", end= " ")
        print(zdanie[poczatek:koniec])

input("\n\n\nAby zakonczyc program, nacisnij Enter")
