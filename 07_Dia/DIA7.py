"""
Exercises: Level 1
Find the length of the set it_companies
Add 'Twitter' to it_companies
Insert multiple IT companies at once to the set it_companies
Remove one of the companies from the set it_companies
What is the difference between remove and discard
"""
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))

it_companies.add("Twitter")

it_companies.update(["Meta", "Gamemaxx", "Razer"])

print(it_companies)

it_companies.remove("Gamemaxx")
print(it_companies)

print("""La diferencia entre discard y remove es que el primero no da error si el valor especifico
no se encuentra en el set, sin embargo remove si arrojará un error""")

"""Exercises: Level 2
Join A and B
Find A intersection B
Is A subset of B
Are A and B disjoint sets
Join A with B and B with A
What is the symmetric difference between A and B
Delete the sets completely"""
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(A.union(B))
print(A.isdisjoint(B)) #falso es que si comparten items
print(A.intersection(B))
print(A.union(B))
print(B.union(A))

print(A.symmetric_difference(B))

del A, it_companies, B, age


