# -*- coding: utf-8 -*-
#!/usr/bin/python



# #3. Napisz program Kto jest twoim tatą?, który umożliwia użytkownikowi
# wprowadzenie imienia i nazwiska osoby płci męskiej i przedstawia imię
# i nazwisko jej ojca. (Możesz dla zabawy wykorzystać nazwiska celebrytów,
# osób fikcyjnych lub nawet postaci historycznych). Umożliw użytkownikowi
# dodawanie, wymianę i usuwanie par syn-ojciec.
#
# 4. Udoskonal program Kto jest moim tatą? poprzez dodanie opcji, która umożliwi
# użytkownikowi wprowadzenie imienia i (lub) nazwiska jakiejś osoby i uzyskanie
# odpowiedzi, kto jest jej dziadkiem. Twój program powinien nadal wykorzystywać
# tylko jeden słownik par syn-ojciec. Pamiętaj, aby włączyć do swojego słownika
# kilka pokoleń, tak aby możliwe było tego rodzaju dopasowanie.

import random
ojcowie = ["Tom Cruise ", "Ferdynand Kiepski", "Donald Tusk", "Krzysztof Ibisz",
"Józef Piłsudzki", "Antoni Macierewicz", "Adam Mickiewicz", "Henryk Sienkiewicz"]
wybor = None
wybor_kolejny = None
rodzina = {}
syn = ""

while wybor != 0:
    print("""
    0 - wyjdz
    1 - sprawdz, kto jest jego ojcem
    2 - wymień ojca
    3 - dodaj ojca
    4 - usuń ojca
    5 - lista wszystkich ojcow
    """)
    wybor = int(input("\nCo wybierasz?\n\n"))
    if wybor == 0:
        print("Do zobaczenia")
    elif wybor == 1:
        syn = input("Wpisz czyjes imie i nazwisko a dowiesz sie kto jest jej ojcem\n")
        if syn not in rodzina:
            ojciec = random.choice(ojcowie)
            rodzina[syn] = ojciec
            print("\nojcem osoby", syn, "jest", rodzina[syn])

            print(""" Czy chcesz poznać, kto jest jego dziadkiem?
                  0 - wyjdz
                  1 - sprawdź
                  """)

            wybor_kolejny = int(input("Co wybierasz?"))

            if wybor_kolejny == 1:
                dziadek  = random.choice(ojcowie)
                if dziadek == ojciec:
                    dziadek  = random.choice(ojcowie)
                else:
                    rodzina[ojciec] = dziadek
                    print("\ndziadkiem", syn, "jest", dziadek, "\n")
        else:
            print("\nojcem", syn, "jest", rodzina[syn])
    elif wybor == 2:
        syn = input("\nCzyjego ojca chcesz zmienić?\n")
        if syn in rodzina:
            nowy_ojciec = input("Podaj nowego ojca\n")
            if nowy_ojciec not in rodzina:
                rodzina[syn] = nowy_ojciec
                if nowy_ojciec not in ojcowie:
                    ojcowie.append(nowy_ojciec)

    elif wybor == 3:
        nowy_ojciec = ""
        nowy_ojciec = input("Podaj imię i nazwisko ojca:\n ")
        if nowy_ojciec not in ojcowie:
            ojcowie.append(nowy_ojciec)

    elif wybor == 4:
        print(ojcowie)
        usuniete_nazwisko = ""
        usuniete_nazwisko = input("Które nazwisko ojca chcesz usunąć?\n")
        if usuniete_nazwisko in ojcowie:
            ojcowie.remove(usuniete_nazwisko)

    elif wybor == 5:
        print(ojcowie)
        print(rodzina)



input("Aby zakonczyc, nacisnij Enter")
