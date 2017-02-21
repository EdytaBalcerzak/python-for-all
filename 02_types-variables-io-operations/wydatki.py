print("""

                           Moje wydatki

                     Analiza moich wydatkow :)""")
dol = int(input("\n\n\n\n\t\t\tWyplata: "))
cosm = int(input("\n\t\t\tKosmetyki: "))
food = int(input("\n\t\t\tJedzenie: "))
tick = int(input("\n\t\t\tBilety: "))
pho = int(input("\n\t\t\tTelefon: "))

total = (dol - (cosm + food + tick + pho))


print("\n\t\t\tLaczna suma: ", total)

input("\n\n\n\t\t\taby wyjsc nacisnij Enter")
