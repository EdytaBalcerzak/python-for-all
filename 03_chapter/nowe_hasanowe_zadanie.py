print("Program liczy punkt przegięcia funkcji kwadratowej")
print("o wyglądzie ax^2 + bx + c")
a = int(input("a="))
b = int(input("b="))
c = int(input("c="))

#Współrzędne wierzchołka paraboli:
#x=-b/2a
#y=-delta/4a
#delta=b^2-4ac

delta=b*b-4*a*c
x=-b/2*a
y=-delta/4*a

print("Współrzędne wirzchołka funkcji kwadratowej:")
print("(x0,y0)=(", x, ",", y ,")")
input("aby zakonczyc program, nacisnij Enter")
