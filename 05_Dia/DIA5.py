#Exercises: Level 1
#=====================================
empty_list = list()
#=====================================
list_with_morefive = list([1, 2, 3, 4, 5, 6, 7])
print(len(list_with_morefive))
print(list_with_morefive[0], list_with_morefive[3], list_with_morefive[-1]) 
#=====================================
mixed_data_types = ["Daniel", 21, 1.66, "married", "Quito"]
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies)
print("number of companies: ", len(it_companies))
print(it_companies[0], it_companies[3], it_companies[-1])
print(it_companies, "sin editar")
it_companies.append("RiotGames")
it_companies.insert(4, "Sony")
it_companies[4] = "SONY"
print(it_companies)
caracters_list = ["#", ";", " "]
print(it_companies + caracters_list)
print(it_companies.count("RiotGames"))
it_companies.sort()
print(it_companies)
it_companies.reverse()
print(it_companies)
print(it_companies[0:3])
print(it_companies[-3:])
print(it_companies[4])
del it_companies[0]
print(it_companies)
del it_companies[4]
print(it_companies)
del it_companies[-1]
print(it_companies)
it_companies.clear()
print(it_companies)
del it_companies
#=====================================
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full_stack = (front_end + back_end)
print(full_stack)

full_stack.insert(4, "Python")
full_stack.insert(4, "SQL")

print(full_stack)

#excersise lvl2

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
print(ages)
print(ages[0], ages[-1])
ages.insert(0, 19)
ages.insert(-1, 26)
print(ages)

mediana = int((24+24)/2)
print("mediana: ", mediana)

sum_ages=sum(ages)

avarage_age = int((sum_ages)/2)
print("Avarage age is: ", avarage_age)

min_age = ages[0]
max_age = ages[-1]
print("max age: ", ages[-1], "min age: ", ages[0])

min_avarage = (min_age-avarage_age)
max_avarage = (max_age-avarage_age) 

print("(min - average): ", abs(min_avarage), "(max - average)", abs(max_avarage))  