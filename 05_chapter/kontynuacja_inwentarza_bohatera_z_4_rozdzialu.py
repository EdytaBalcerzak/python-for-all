#zamiast krotek tworzę listy (w nawiasie kwadratowym)

plecak = ["miecz", "zbroja", "tarcza", "dezodorant", "złoto", "papierosy"]
print("Oto zawartość Twojego inwentarza:")
for rzeczy in plecak:
    print(rzeczy)
print("Posiadasz", len(plecak), "rzeczy")
input("\nAby kontynuować, nacisnij Enter")
#przypisanie nowej wartosci elementowi listy poprzez indks
print("\nWymieniasz swój miecz na kuszę.")
print("Twój aktualny inwentarz to:\n")
plecak[0] = "kusza"
print(plecak)
input("\nAby kontynuować, nacisnij Enter")
#przypisanie nowej wartości wycinkowi listy
print("\nZużywasz swoje złoto i papierosy na zakup kuli do wróżenia")
plecak[4:6] = ["kula do wróżenia"]
print("Twój aktualny inwentarz to:")
for rzeczy in plecak:
    print(rzeczy)

input("\nAby kontynuować, nacisnij Enter")
#usuniecie elementu listy
print("\nW wielkiej bitwie Twoja tarcza ulega uszkodzeniu")
del plecak[2]
print("\nW Twoim plecaku znajdziesz teraz:")
print(plecak)
input("\nAby kontynuować, nacisnij Enter")
#usunięcie wycinka listy
print("\nNapotkałeś rabusi, którzy rozebrali Cię, zgwałcili oraz ukradli zbroję i kuszę")
del plecak[:2]
print("Na szczęście nie potrzebowali reszty rzeczy")
print("\nTwój aktualny inwentarz to:")
for rzeczy in plecak:
    print(rzeczy)
print("\nW Twoim plecaku są", len(plecak), "rzeczy")







input("\n\n\nAby zakonczyc program, nacisnij Enter")
