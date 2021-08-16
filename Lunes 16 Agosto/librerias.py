import math

print("EJERCICIO 1")
radio = float(input("Dime el radio: "))
area = 4 * math.pi * radio ** 2
print(area)

print("EJERCICIO 2 \n")
a = float(input("Dime a: "))
b = float(input("Dime b: "))
c = float(input("Dime c: "))
s = (a + b + c) / 2
area = math.sqrt(s * (s-a) * (s-b) * (s-c))
print(area)


