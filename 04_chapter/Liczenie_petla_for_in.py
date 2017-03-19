#program liczący za użytkownika
pierwsza_liczba = int(input("Podaj pierwszą liczbę"))
druga_liczba = int(input("Podaj drugą liczbę"))
roznica = int(input("Co ile mam liczyć?"))
for i in range(pierwsza_liczba, druga_liczba, roznica):
    print(i, end=" ")

input("\n\nAby zakonczyć program, naciśnij Enter")
