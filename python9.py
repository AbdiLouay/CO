import math

# Demander les coefficients à l'utilisateur
a = float(input("Entrez le coefficient a: "))
b = float(input("Entrez le coefficient b: "))
c = float(input("Entrez le coefficient c: "))

# Calculer le déterminant
D = b**2 - 4*a*c

if D < 0:
    print("L'équation n'a pas de solutions réelles.")
elif D == 0:
    # Calculer l'unique solution
    x = -b / (2*a)
    print(f"L'équation a une unique solution: x = {x}")
else:
    # Calculer les deux solutions
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print(f"L'équation a deux solutions: x1 = {x1}, x2 = {x2}")