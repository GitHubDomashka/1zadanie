a=float(input("Введите длину большой полуоси"))
b=float(input("Введите длину малой полуоси"))
pi=3.14

S=a*b*pi
P=4*(((pi*a*b)+(a-b))/(a+b))

print(float(S))
print(float(P))
