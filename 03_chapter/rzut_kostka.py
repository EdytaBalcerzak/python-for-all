print("\t\t\tRzut koscmi")

import random

kostka1 = random.randint(1, 6)
kostka2 = random.randrange(6) + 1
kostka3 = random.randint(1, 6)

total = kostka1 + kostka2 + kostka3
print("Wyrzuciles ", kostka1, " oraz ", kostka2, " a nawet ", kostka3,"\nUzyskales sume", total, "oczek")
input("aby zakonczyc program nacisnij Enter")
