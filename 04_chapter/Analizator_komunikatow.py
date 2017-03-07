#program analizuje komunikat
#liczy ilosc znakow oraz sprawdza czy wystepuje w nim litera a

print("\n\n\t\t\tAnalizator komunikatow")

message = input("Wprowadz jakies zdanie\n\n")

print("Dlugość Twojego komunikatu wynosi: ", len(message))
if "a" in message:
    print("W Twojej wiadomosci wystapiła litera 'a',")
else:
    print("W Twojej wiadomosci nie wystąpiła litera 'a'")

input("Aby zakonczyc program , nacisnij Enter")
