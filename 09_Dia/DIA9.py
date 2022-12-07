"""Get user input using input(“Enter your age: ”). 
If user is 18 or older, give feedback: You are old enough to drive. 
If below 18 give feedback to wait for the missing amount of years."""

"""
user_age = int(input("Enter your age: "))

if user_age >= 18:
    print("You are old enough to drive")
elif user_age < 18:
    missing_age = (18 - user_age)
    print(f"U have to wait {missing_age} years :D")
    """

"""
Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) 
to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age,
 'years' for bigger differences, 
and a custom text if my_age = your_age"""

"""
my_age = int(input("My age is: "))
your_age = int(input("Enter your age: "))
age_diference = abs(my_age-your_age)

if my_age>your_age:
    if age_diference == 1:
        print(f"I\"m {age_diference} year older than you")
    else:
        print(f"I\"m {age_diference} years older than you")
elif my_age == your_age:
    print("we have the same age! :D") 
else:
    if age_diference == 1:
        print(f"You are {age_diference} year older than me")
    else:
        print(f"You are {age_diference} years older than me")
        """
    

#Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

"""
number_one = (input("Ingresa el numero A "))
number_two = (input("Ingresa el numero B "))

if number_one > number_two:
    print(f"{number_one} is greater than {number_two}")
elif number_one < number_two:
    print(f"{number_two} is greater than {number_one}")
else:
    print(f"{number_one} and {number_two} are the same number :D")
"""

"""
Write a code which gives grade to students according to theirs scores:

80-100, A
70-79, B
60-69, C
50-59, D
0-49, F
"""

"""
grades = {"A":list(range(80,101)), 
"B":list(range(70, 80)),
"C":list(range(60, 70)),
"D":list(range(50, 60)),
"F":list(range(0, 50))}


notas_estudiantes = {}

nombre_estudiante = input("Ingrese el nombre del estudiante: ")
calificación_estudiante = int(input("ingrese la calificación del estudiante: "))

notas_estudiantes["nombre"] = nombre_estudiante
notas_estudiantes["grade"] = calificación_estudiante

if calificación_estudiante in grades["A"]:
    print("A")
elif calificación_estudiante in grades["B"]:
    print("B")
elif calificación_estudiante in grades["C"]:
    print("C")
elif calificación_estudiante in grades["D"]:
    print("D")
elif calificación_estudiante in grades["F"]:
    print("F")
"""


"""
Check if the season is Autumn, Winter, Spring or Summer. If the user input is: 
September, October or November, the season is Autumn.
December, January or February, the season is Winter.
March, April or May, the season is Spring 
June, July or August, the season is Summer
"""

"""
autumn_months = {"September", "October", "November"}
winter_months = {"December", "January", "February"}
spring_months = {"March", "April", "May"}
summer_months = {"June", "July", "August"}

actual_month = input("Ingresa el mes actual: ").capitalize()

if actual_month in autumn_months:
    print("The actual season is autumn")
elif actual_month in winter_months:
    print("The actual season is winter")
elif actual_month in spring_months:
    print("The actual season is spring")
elif actual_month in summer_months:
    print("The actual season is summer")
"""

"""
The following list contains some fruits:

fruits = ['banana', 'orange', 'mango', 'lemon']
If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
If the fruit exists print('That fruit already exist in the list')
"""

"""
fruits = ['banana', 'orange', 'mango', 'lemon']

ingresed_fruit = input("Ingrese una fruta: ").lower()

if ingresed_fruit in fruits:
    print("la fruta ingresada ya se encuentra en la lista :D")
else:
    fruits.append(ingresed_fruit)
    print(f"se ha agregado {ingresed_fruit} a la lista de frutas, su nueva lista es {fruits}")
"""

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': "Finland",
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
front_end_skills = ["JavaScript", "React"]
back_end_skills = ["Node", "MongoDB", "Python"]

if "skills" in person:
    middle_skill = person.get("skills")    
    #print("The middle skill is: ", middle_skill[2])
    if "Python" in person['skills']:
        print("Python is one of the skills! :D")
    if person['skills'] == front_end_skills:
        print('He is a front end developer')
    elif person['skills'] == back_end_skills:
        print("He is a back end developer")

if person['is_marred'] == True and person['country'] == "Finland":
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He\'s married")



