#Day 2: 30 Days of python programming ahora con variables ugu
"""
Declare a first name variable and assign a value to it
Declare a last name variable and assign a value to it
Declare a full name variable and assign a value to it
Declare a country variable and assign a value to it
Declare a city variable and assign a value to it
Declare an age variable and assign a value to it
Declare a year variable and assign a value to it
Declare a variable is_married and assign a value to it
Declare a variable is_true and assign a value to it
Declare a variable is_light_on and assign a value to it
Declare multiple variable on one line

"""

first_name = "Daniel"
last_name = "Salas"
full_name = "Daniel Salas"
country = "Ecuador"
city = "Quito"
age = 21
year = 2022
is_married = "En compromiso"
is_true = "sisas"
is_light = "maomeno"

cuantas_pc, grafica, discos, telefono = 2, "gtx 1650", 2, "Mi10T"

print(type(first_name))
print(type(age))

#ejercicio 2

longitud = len(first_name)
print(longitud)

longitud_last = len(last_name)
print(longitud_last)

print("primer nombre tiene", longitud, "caracteres, mientras que, apellido tiene", longitud_last, "caracteres")

#ejercio 4

num_one = 5
num_two = 4

variable_total = num_one + num_two
print("5+4 es", variable_total)

variable_diff = num_one - num_two
print("5-4 es", variable_diff)

variable_product = num_one * num_two
print("5*4 es", variable_product)

variable_division = num_one / num_two
print("5/4 es", variable_division)

variable_remainder = num_two % num_one
print("4%5 es", variable_remainder)

variable_exp = num_one ** num_two
print("5**4 es", variable_exp)

floor_division = num_one // num_two
print("5//4 es", floor_division)


#si el radio de un circulo es 30 calcular
"""
1. Calculate the area of a circle and assign the value to a variable name of area_of_circle
2. Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
3. Take radius as user input and calculate the area.

"""
import math
#1

pi = math.pi
r = 30
area_of_circle = pi*(r**2)
print("dado que el radio es:", r)
print("El area del circulo es:", int(area_of_circle))

#2
pi = math.pi
r = 30 
circum_of_circle = 2*pi*r
print("dado que el radio es:", r)
print("La circunferencia es de:", int(circum_of_circle))

#3

pi = math.pi
r = float(input("ingrese el radio del circulo "))
area_of_circle = pi*(r**2)
print("Segun el radio escogido:", r)
print("El area del circulo es de:", round(area_of_circle, 2))

