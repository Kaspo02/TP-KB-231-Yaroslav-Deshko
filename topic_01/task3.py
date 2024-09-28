def discriminant(a: float, b: float, c: float) -> float:
    return pow(b, 2) - 4*a*c

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

print(discriminant(a, b, c))