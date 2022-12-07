"""Exercises: Level 1
Create an empty tuple
Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
Join brothers and sisters tuples and assign it to siblings
How many siblings do you have?
Modify the siblings tuple and add the name of your father and mother and assign it to family_members"""

my_empty_tuple = ()
my_brothers_tuple = ("Pablo", "Oswaldo", "Luis")
my_sisters_tuple = ("Charlotte", "Val", "Lucia")

my_sibilings_tuple = my_brothers_tuple + my_sisters_tuple

print(len(my_sibilings_tuple))

family_members = list(my_sibilings_tuple)

family_members.insert(0, "Monica")
family_members.insert(0, "Oswaldo")

print(family_members)

"""
Exercises: Level 2
Unpack siblings and parents from family_members
Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
Change the about food_stuff_tp tuple to a food_stuff_lt list
Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
Slice out the first three items and the last three items from food_staff_lt list
Delete the food_staff_tp tuple completely
Check if an item exists in tuple:
Check if 'Estonia' is a nordic country

Check if 'Iceland' is a nordic country

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')"""

a, b, c, d, e, f, g, h = family_members

print(a)
print(b)

fruits = "manzana", "pera", "durazno"
vegetables = "lechuga", "cilantro", "culantro"
animales = "vaca", "cerdo", "ternera"

food_stuff_tp = fruits+vegetables+animales
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_tp)
print(type(food_stuff_lt)) 

print(food_stuff_lt[4])

print(food_stuff_lt[0:3])
print(food_stuff_lt[-3:])

del food_stuff_tp


nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)