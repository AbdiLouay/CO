
import math

    #initialisation des variables
a=0
b=200
h=0

N=int(input("entrez le nombre de température"))
Total=0
Moyenne=0

    #Acquisitions et Calculs des Températures
while (a < N):
  a=a+1
  print("Entrez température :")

  Température=float(input())
  Total=Total+Température            #Calcul Total
  if Température < b:                #Recherche nombre min
    b = Température
  if Température > h:                #Recherche nombre max
    h = Température
Moyenne=Total/N                      #Calcul Moyenne
étendu=h-b                           #Calcul étendu

    #Affichage des résultats
print("La somme total des température est de",round(Total,1) ,"°C")
print("La moyenne des température est de",round(Moyenne,1) ,"°C")
print("La température minimale est de",round(b,1),"°C")
print("La température maximale est de",round(h,1),"°C")
print("L'étendu est de",round(étendu, 1))