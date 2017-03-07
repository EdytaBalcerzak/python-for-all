#Program ukazujacy petle for na liczbach
print("\n\n\nLiczenie po kolei\n")
for i in range(10):
    print(i, end = ", ")
print("\n\nliczenie co kilka liczb\n\n")
for i in range(1, 31, 3):
    print(i, end = ", ")
print("\n\nLiczenie do tylu\n\n")
for i in range(32, 0, -4):
    print(i, end = ", ")

input("\n\n\nAby zakonczyc program , nacisnij Enter")
