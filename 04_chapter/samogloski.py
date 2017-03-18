wiadomosc = input("Wprowadz jakies zdanie:  ")
nowa_wiadomosc = ""
SAMOGLOSKI = "aąjioeęyuó"
print()
for letter in wiadomosc:
    if letter not in SAMOGLOSKI:
        nowa_wiadomosc += letter
        print("Została utworzona nowa wiadomosc", nowa_wiadomosc)
input("\n\n\nAby zakonczyc program, nacisnij Enter")
