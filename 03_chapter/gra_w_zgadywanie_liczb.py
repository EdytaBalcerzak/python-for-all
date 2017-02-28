print("\n\n\t\t\tGra w zgadywanie liczb\n\n\n")
print("Wybralam dla Ciebie liczbe z zakresu od 1 do 100")
print("Sprobuj ja odgadnac\n\n\n")
import random
number = random.randint(1,100)
guess_number = int(input("Jak myslisz, jaka to liczba? \n"))
tries = 1
while number != guess_number:
    if number > guess_number:
        print("Liczba jest za mala. Sprobuj jeszcze raz")
        tries += 1
    elif number < guess_number:
        print("Liczba jest za duza. Sprobuj jeszcze raz")
        tries += 1
    guess_number = int(input("\nJak myslisz, jaka to liczba? \n"))

print("Brawo! Zgadles!")
print("Potrzebowales", tries, "prob")

input("\n\n\nAby zakonczyc program, nacisnij Enter")
