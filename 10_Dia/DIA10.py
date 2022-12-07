count = 0

while count < 11:
    print(count)
    count += 1

print("=================")

for count in range(0, 11):
    print(count)

ejemplo="#"

#Write a loop that makes seven calls to print(), so we get on the output the following triangle:

repeticiones = range(1,8)

for multiplicador in repeticiones:
    print(ejemplo*multiplicador)
print("=================")
ejercicio = "# "
patron = ejercicio
repeticiones = range(1,9)

for multiplicador in repeticiones:
    print(patron*8) #aunque no use nested, está bien xd

print("=================")

for numero in range(0, 11):
    multiplicación = numero*numero
    print(f"{numero}*{numero}: {multiplicación}")

print("=================")

lista = ['Python', 'Numpy','Pandas','Django', 'Flask']

for dat in lista:
    print(dat)
print("=================")

#ta como comentario pq tiene input, pa usarlo quitale las comillas
"""solicitud=input("Quieres pares o nones ")

if solicitud == "pares":
    for number in range(0,11,2):
        print(number)
elif solicitud != "nones":
    print("elije pares o nones")
else:
    for number in range(1, 11, 2):
        print(number)"""

#forma más facil pero bueno, me piden loops xd
"""
numbers = range(0, 101)
print(sum(numbers))
"""
numbers = range(0, 101)
base=0
for digits in numbers:
    base+=digits
else:
    print(base)

print("====================")
base=0
base2=0

for evens_digits in range(0, 101, 2):
    base+=evens_digits
for odd_digits in range(1, 101, 2):
     base2+=odd_digits
else:
    print(f"The sum of all evens is {base}. And the sum of all odds is {base2}.")

fruit_list = ['banana', 'orange', 'mango', 'lemon']
print(f"after reverse: {fruit_list}")
reversed_list=[]
for data in fruit_list:
    reversed_list = [data] + reversed_list
print(f"before reverse {reversed_list}")

