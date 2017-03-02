# Program Ciasteczko z wróżbą
# Dokonuje losowego wyboru przy każdym uruchomieniu programu

print("Program z Ciasteczkowymi wróżbami")


import random
wrozba_losowa = random.randint(1, 6)
print("\n\nOto Twoja wróżba na dziś")
if wrozba_losowa == 1:
    print("\n\nNie oglądaj się za siebie.")
elif wrozba_losowa == 2:
    print("\n\nTeraz pójdzie gładko.")
elif wrozba_losowa == 3:
    print("\n\nBez odwagi nie zostaniesz dowódcą.")
elif wrozba_losowa == 4:
    print("\n\nTeraz twoja kolej.")
elif wrozba_losowa == 5:
    print("\n\nJeśli zdobędziesz się na cierpliwość w jednej chwili gniewu, zaoszczędzisz sobie sto dni przykrości.")
elif wrozba_losowa == 6:
    print("\n\nJeśli nikogo się o nic nie prosi, wszyscy wydają się uczynni.")


input("\n\n\nAby zakonczyc program, nacisnij Enter")
