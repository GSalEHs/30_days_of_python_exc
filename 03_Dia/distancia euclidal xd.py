#sacar distancia euclidal y pendiente de (2, 2) ; (6,10)
separador_wii = "======================================"

from math import dist

x1, x2, y1, y2 = 2, 6, 2, 10 

punto1 = (x1, y1)
punto2 = (x2, y2)

distancia_euc = dist(punto1, punto2)

m = (y2 - y1)/(x2 - x1)

print("dado los puntos:", punto1, "y", punto2 )
print("la distancia euclidal es de: ", round(distancia_euc, 2))
print("la pendiente es de: ", m)

print(separador_wii)

#encontrar el valor de y, descubrir cual x hace que el mismo sea 0
#y (y = x**2 + 6x + 9)

x = int(input("Ingrese un valor de x "))

y = (x**2 + 6*x + 9)

print("valor de y=", y)

print("y = 0? ", y == 0)

print(separador_wii)

