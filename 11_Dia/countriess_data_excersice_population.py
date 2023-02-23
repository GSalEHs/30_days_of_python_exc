from countries_data import countries_data_lst
from operator import itemgetter
"""
Go to the data folder and access the countries-data.py file.
Create a function called the most_spoken_languages in the world. It should return 10 or 20 
most spoken languages in the world in descending order
Create a function called the most_populated_countries. 
It should return 10 or 20 most populated countries in descending order."""
def most_populated_countries(database):
    if isinstance(database, list):
        countrie_name_key_lst = []
        population_value_lst = []
        for person_dict in database:
            data_index = database.index(person_dict)
            ind_data = database[data_index]
        for name_key in database:
            name_key_value = name_key["name"]
            countrie_name_key_lst.append(name_key_value)
        for population_key in database:
            population_key_value = population_key["population"]
            population_value_lst.append(population_key_value)
        countrie_total_dict = dict.fromkeys(countrie_name_key_lst)
        countrie_total_dict.update(zip(countrie_total_dict, population_value_lst))
        countrie_sorted_tuple = sorted(countrie_total_dict.items(), key=itemgetter(1), reverse=True)
        ten_most_populated = dict(countrie_sorted_tuple[0: 20]).keys()
        print(f"the 20 most populated countries in the world are: {ten_most_populated}")
    else:
        print(f"{database} no es una lista")

most_populated_countries(countries_data_lst)

