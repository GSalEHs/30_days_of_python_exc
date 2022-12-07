"""
Create an empty dictionary called dog
Add name, color, breed, legs, age to the dog dictionary
Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
Get the length of the student dictionary
Get the value of skills and check the data type, it should be a list
Modify the skills values by adding one or two skills
Get the dictionary keys as a list
Get the dictionary values as a list
Change the dictionary to a list of tuples using items() method
Delete one of the items in the dictionary
Delete one of the dictionaries"""

dog = {}
dog.update({"name":"lulu", "color":"black", "breed":"husky", "legs":4, "age":15})
print(dog)

student_dict = {
    "first_name":"Daniel", 
    "last_name":"Salas", 
    "gender":"men", 
    "age":21, 
    "marital_status":"married", 
    "skills":["coding", "gaming", "maths"], 
    "country":"ecuador", 
    "city":"quito", 
    "address":"paccha"}
print(len(student_dict))
print(type(student_dict["skills"]))
student_dict["skills"] += ["rubik solve", "it"]
print(student_dict)

print(list(student_dict.keys()))
print(list(student_dict.values()))

student_tuple = tuple(student_dict.items())
print(student_tuple)
print(type(student_tuple))

del student_dict["address"]
print("===========================")
print(student_dict)

del student_dict

