# program ukazujacy warunki zlozone
print ("\t\t\t\nWitaj na portalu Mowie co mysle")
print("Zaloguj sie")


security = 0
username = ""
while not username:
    username = input("Podaj swoj nickname")
password = ""
while not password:
    password = input("Podaj swoje haslo")
if username == "hasan" and password == "wyhasany":
    print("Witaj Misiurku")
    security = 3
elif username == "edyta" and password == "programistka":
    print("Witaj na portalu")
    security = 5
elif username == "gosc" and password == "gosc":
    print("Witaj gosciu")
    security = 1
else:
    print("Konto nie istnieje")
input("\t\t\t\n\n\naby zakonczyc program , nacisnij Enter")
