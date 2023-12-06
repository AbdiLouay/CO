from math import *
def resol_second_degre (a,b,c):

    if a !=0:
        delta = b**2-4*a*c

        if delta < 0:
            return ("il à pas solution réelle")
        elif delta == 0:
            x = -b / (2*a)
            return ("il y a une solution réelle" + str(x))
        else:
            x1 = (-b-sqrt(delta)) / (2*a)
            x2 = (-b+sqrt(delta)) / (2*a)
         return ("il y a deux solution réelle" + str(x1) + "et" + str(x2))
    else;
        return("a=0. ce n'est pas uen fonction du second degré")
        