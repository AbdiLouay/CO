from math import*

def display_solution(x1, x2):
    return "Les solutions sont: " + str(x1) + " et " + str(x2)

def resol_second_degre (a,b,c):
    if a !=0:
        delta = b**2-4*a*c

        if delta < 0:
            return "il à pas solution réelle"
        elif delta == 0:
            x = -b / (2*a)
            return display_solution(x, x)
        else:
            x1 = (-b-sqrt(delta)) / (2*a)
            x2 = (-b+sqrt(delta)) / (2*a)
            return display_solution(x1, x2)
    else:
        return "la première coordonnée n'est pas égale à 0"

print(resol_second_degre(1,-3,2))
print(resol_second_degre(0,-3,2))