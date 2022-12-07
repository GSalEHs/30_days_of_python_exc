#calcular puntos de intersección y pendiente de y=2x-2
separador_wii = "======================================"

print("Pendiente con interfaz")

x1 = float(input("Ingrese punto x1 "))
y1 = float(input("Ingrese punto y1 "))
x2 = float(input("Ingrese punto x2 "))
y2 = float(input("Ingrese punto y2 "))

m = (y2 - y1)/(x2 - x1)

print("La pendiente es igual a: ", m)

print(separador_wii)

x1 = 0
y1 = (2 * x1 - 2)
print("Intersección y= ", "x= ", x1, "y= ", y1 )

x2 = 1
y2 = (2 * x2 - 2)

print("Intersección x= ", "x= ", x2, "y= ", y2 )

m = (y2 - y1 )/(x2 - x1)

print("dado esto, la pendiente es= ", m )