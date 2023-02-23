#Exercises: Level 1
import math

#Declare a function add_two_numbers. It takes two parameters and it returns a sum.

def add_two_numbers(first_parameter, second_parameter):
    sum_of_numbers=first_parameter+second_parameter
    print(f"the sum of {first_parameter} and {second_parameter} is:{sum_of_numbers} ")

add_two_numbers(15, 5)

#Area of a circle is calculated as follows: area = π * r**2. Write a function that calculates area_of_circle.



def circle_area_calculator(radius):
    pi=math.pi
    area = round((pi*(radius**2)), 2 )
    print(f"the area of the circle with radius: {radius} is {area}")

circle_area_calculator(30)
#with input funct
"""
def circle_area_calculator(radius=int(input("What is the radius of the circle? "))):
    pi=math.pi
    area = round((pi*(radius**2)), 2 )
    print(f"the area of the circle with radius: {radius} is {area}")

circle_area_calculator()"""


#Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments.
#Check if all the list items are number types. If not do give a reasonable feedback.


def add_all_nums(*argument):
    list_of_args = []
    for value in argument:
        if isinstance(value, (int, float)):
            list_of_args.append(value)
            continue
        else:
            print(f"{value} no es un numero")
            break
    else:
        return sum(list_of_args)

print(add_all_nums(1, 2, 3, 1.5))

#Temperature in °C can be converted to °F using this formula: 
#°F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.

def convert_celsius_to_fahrenheit(celcius):
    c=celcius
    f= round((c*(9/5)+32),2)
    print(f"{c} grados celcius son {f} grados fahrenheit")

convert_celsius_to_fahrenheit(30)

#Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.

def check_season(month):
    
    autumn_months = {"September", "October", "November"}
    winter_months = {"December", "January", "February"}
    spring_months = {"March", "April", "May"}
    summer_months = {"June", "July", "August"}
    if isinstance(month, str):
        cap_month= month.capitalize()
        if cap_month in autumn_months:
            print("The actual season is autumn")
        elif cap_month in winter_months:
            print("The actual season is winter")
        elif cap_month in spring_months:
            print("The actual season is spring")
        elif cap_month in summer_months:
            print("The actual season is summer")
        else:
            print("Enter a valid month")
    else:
        print("Enter a valid argument")


check_season("december")

#Write a function called calculate_slope which return the slope of a linear equation

def calculate_slope(x1, x2, y1, y2):
    if isinstance(x1, int) and isinstance(x2, int) and isinstance(y1, int) and isinstance(y2, int):
        m = round(((y2 - y1)/(x2 - x1)), 2)
        print(m)
    else:
        print("enter valid arg")

calculate_slope(1, 2, 4, 0)

#Quadratic equation is calculated as follows: ax² + bx + c = 0. 
#Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.

def solve_quadratic_eqn(a, b, c):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float)):
        rq = math.sqrt((b**2)-(4*a*c))

        fpos = (-b + rq)/(2*a)
        fneg = (-b - rq)/(2*a)

        print("positive solve:", round(fpos, 2))
        print("negative solve:", round(fneg, 2))
    else: 
        print("Enter a valid arg")

solve_quadratic_eqn(1, -4, 3)


#Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.

def print_list(list_arg):
    if isinstance(list_arg, list):
        for element in list_arg:
            print(element)
    else:
        print("Ingrese una lista correcta")
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print_list(ages)

#Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
def reverse_list(arg_to_reverse):
    reversed_list = []
    if isinstance(arg_to_reverse, list):
        while arg_to_reverse:
            poped_item = arg_to_reverse.pop(-1)
            reversed_list.append(poped_item)
        print(reversed_list)

reverse_list(ages)
#Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(arg_to_cap):
    capitalizated_list= []
    if isinstance(arg_to_cap, list):
        for arg in arg_to_cap:
            if isinstance(arg, str):
                 capitalizated_list.append(arg.capitalize())
            else:
                (f"{arg} is not an str")
        print(capitalizated_list)
    else:
        print("enter a valid list")

food_staff = ['potato', 'tomato', 'mango', 'milk']
capitalize_list_items(food_staff)

#Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
food_staff = ['potato', 'tomato', 'mango', 'milk']
def add_item(objetive_list, to_add_value):
    if isinstance(objetive_list, list):
        objetive_list.append(to_add_value.lower())
        print(objetive_list)
    else:
        print(f"{objetive_list} is not a list!")

add_item(food_staff, "Chocolate")

#Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
food_staff = ['potato', 'tomato', 'mango', 'milk']
def remove_item(objetive_list, to_remove_value):
    if isinstance(objetive_list, list):
        value_index = objetive_list.index(to_remove_value)
        del objetive_list[value_index]
        print(objetive_list)
    else:
        print(f"{objetive_list} is not a list!") 

remove_item(food_staff, "mango")

#Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.

def sum_of_odds(odds_arg):
    if isinstance(odds_arg, int):
        stop_range_arg= odds_arg+1
        range_to_sum= range(1,stop_range_arg,2)
        sum_total = sum(range_to_sum)
        print(f"{sum_total} is the sum :D")
    else:
        print(f"{odds_arg} is not a number int")

sum_of_odds(10)

#Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.

def sum_of_even(even_arg):
    if isinstance(even_arg, int):
        stop_range_arg= even_arg+1
        range_to_sum= range(0,stop_range_arg,2)
        sum_total = sum(range_to_sum)
        print(f"{sum_total} is the sum :D")
    else:
        print(f"{even_arg} is not a number int")

sum_of_even(10)

#Exercises: Level 2
#Declare a function named evens_and_odds . 
#It takes a positive integer as parameter and it counts number of evens and odds in the number.

def evens_and_odds(number):
    if isinstance(number, int):
        range_number = number+1
        odds_list= []
        odds_list.extend(range(1, range_number, 2))
        len_odds=len(odds_list)
        print(f"odds numbers in {number} are {len_odds}")
        
        even_list=[]
        even_list.extend(range(0, range_number, 2))
        len_even= len(even_list)
        print(f"even number in {number} are {len_even}")
    else:
        print(f"{number} is not a int number")
        

evens_and_odds(100)

#Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(number):
    if isinstance(number, int):
        items_to_mult = []
        range_number = number + 1
        producto = 1
        items_to_mult.extend(range(1, range_number))
        for items in items_to_mult:
            producto *= items
        print(f"{producto} es el numero factorial de {number}")
    else:
        print(f"{number} no es un numero entero!")


factorial(5)

#Call your function is_empty, it takes a parameter and it checks if it is empty or not
 
def is_empty(arg):
    if not arg ==True:
        print("ta vacio")
    else:
        print("ta llenito ugu")

is_empty([])

#Write different functions which take lists. 
#They should calculate_mean, calculate_median, calculate_mode, calculate_range, 
#calculate_variance, calculate_std (standard deviation).

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

def calculate_mean(list_arg):
    if isinstance(list_arg, list):
        sum_of_lst = sum(list_arg)
        lst_lengh = len(list_arg)
        mean= sum_of_lst/lst_lengh
        print(mean)
    else:
        print(f"{list_arg} no es una lista! ")

calculate_mean(ages)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

def calculate_median(list_arg):
    if isinstance(list_arg, list):
        ordered_lst = sorted(list_arg)
        lst_lenght = len(ordered_lst)
        middle_index = int(lst_lenght/2)
        print(ordered_lst[middle_index])
        print(ordered_lst)

         
from operator import itemgetter
calculate_median(ages)
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
def calculate_mode(list_arg):
    if isinstance(list_arg, list):
        counted_items_lst = []
        for arg in list_arg:
            number = list_arg.count(arg)
            counted_items_lst.append(number)
        counted_items_dict = dict.fromkeys(list_arg)
        counted_items_dict.update(zip(counted_items_dict, counted_items_lst))
        print(counted_items_dict)
        counted_items_tuple= sorted(counted_items_dict.items(), key = itemgetter(1))
        most_popular_keys = dict(counted_items_tuple).keys()
        most_popular_keys_lst = list(most_popular_keys)
        print(f"the mode is: {most_popular_keys_lst[-1]}")

calculate_mode(ages)

ages = [5, 6, 6, 7, 8]

def calculate_variance(pop_muest, list_arg):
    pop_muest.lower()
    items_to_sum = []
    if isinstance(list_arg, list):
        sum_of_lst = sum(list_arg)
        lst_lengh = len(list_arg)
        mean= sum_of_lst/lst_lengh
        for item in list_arg:
            rest_cuadratic = ((item-mean)**2)
            items_to_sum.append(rest_cuadratic)
        if pop_muest == "poblacion" or pop_muest == "población":
            dividendo_pop= sum(items_to_sum)
            divisor_pop = len(list_arg)
            variance_pop = round((dividendo_pop/divisor_pop), 2)
            print(f"La varianza de la {pop_muest} es {variance_pop}")
        elif pop_muest == "muestra":
            dividendo_muest= sum(items_to_sum)
            divisor_muest = len(list_arg)-1
            variance_muest = round((dividendo_muest/divisor_muest), 2)
            print(f"La varianza de la {pop_muest} es {variance_muest}")
    else:
        print(f"{list_arg} no es una lista! ")

calculate_variance("poblacion", ages)
ages = [5, 6, 6, 7, 8]
def calculate_std(pop_muest, list_arg):
    pop_muest.lower()
    items_to_sum = []
    if isinstance(list_arg, list):
        sum_of_lst = sum(list_arg)
        lst_lengh = len(list_arg)
        mean= sum_of_lst/lst_lengh
        for item in list_arg:
            rest_cuadratic = ((item-mean)**2)
            items_to_sum.append(rest_cuadratic)
        if pop_muest == "poblacion" or pop_muest == "población":
            dividendo_pop= sum(items_to_sum)
            divisor_pop = len(list_arg)
            std_pop = round((math.sqrt(round((dividendo_pop/divisor_pop), 2))),2)
            print(f"La desviacion estandar de la {pop_muest} es {std_pop}")
        elif pop_muest == "muestra":
            dividendo_muest= sum(items_to_sum)
            divisor_muest = len(list_arg)-1
            std_muest = round((math.sqrt(round((dividendo_muest/divisor_muest), 2))),2)
            print(f"La desviacion estandar de la {pop_muest} es {std_muest}")
    else:
        print(f"{list_arg} no es una lista! ")


calculate_std("poblacion", ages)


def is_prime(number):
    if isinstance(number, int):
        for divisor in range(2, number):
            if (number%divisor) == 0:
                print(f"{number} no es primo")
                break
        else:
            print(f"{number} es primo")
    else:
        print(f"{number} no es un valor valido")


is_prime(98)

ages = [19, 22, 24, 20, 25, 26, 24, 25, 24]

def all_items_unique(list_arg):
    if isinstance(list_arg, list):
        for item in list_arg:
            if (list_arg.count(item)) > 1:
                print(f"{item} no es unico en la lista")
                break
#opcional
"""            elif (list_arg.count(item)) == 1:
                print(f"{item} es unico en la lista :D")
            else:
                print(f"{item} no está en la lista :c")
                break"""
        
all_items_unique(ages)


#Write a function which checks if all the items of the list are of the same data type.
ages = [19, 22, 24, 20, 25, 26, 24, 25, 24]
def are_the_same_type(tipo_requerido, list_arg):
    if all(isinstance(item, tipo_requerido) for item in list_arg):
        print(f"todos los tipos {tipo_requerido}  en la lista son los mismos :D ")
    else:
        print("los items no son todos del mismo tipo we :/")

are_the_same_type(int, ages)


