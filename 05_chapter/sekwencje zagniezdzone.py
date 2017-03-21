#sekwencje zagnieżdżone
wyniki = [["ela", 1345], ["gucio", 32], ["sylwia", 321]]
wyniki.sort()
for lista in wyniki:
    print(lista)
#uzyskiwanie dostępu do elementów sekwencji zagnieżdżonych
print(wyniki[0])
print(wyniki[2])
print(wyniki[2][0])
print(wyniki[0][1])
#rozpakowanie sekwencji
imie, wynik = ["ela", 1345]
print(imie)
print(wynik)
input("Aby zako.")
