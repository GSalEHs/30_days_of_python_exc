from countries_data import countries_data_lst
from operator import itemgetter
"""
Go to the data folder and access the countries-data.py file.
Create a function called the most_spoken_languages in the world. It should return 10 or 20 
most spoken languages in the world in descending order
Create a function called the most_populated_countries. 
It should return 10 or 20 most populated countries in descending order."""
def most_spoken_languages(database):
    if isinstance(database, list):
        total_languages=0
        total_lan_values=[]
        number_rep_lan_lst=[]
        countrie_name_key_lst = []
        for person_dict in database:
            data_index = database.index(person_dict)
            ind_data = database[data_index]
            number_languages = len(ind_data["languages"])
            total_languages+=number_languages
            for lan_value in ind_data["languages"]:
                total_lan_values.append(lan_value)
        for ind_lan_value in total_lan_values:
            number_rep_lan = total_lan_values.count(ind_lan_value)
            number_rep_lan_lst.append(number_rep_lan)
        lang_total_dict = dict.fromkeys(total_lan_values)
        lang_total_dict.update(zip(lang_total_dict, number_rep_lan_lst))
        lang_sorted_tuple = sorted(lang_total_dict.items(), key=itemgetter(1), reverse=True)
        ten_more_items = dict(lang_sorted_tuple[0: 20])
        print(f"the 20 most spoken languages are: {ten_more_items}")
        print(f"total languages in the database are: {total_languages} ")
    else:
        print(f"{database} no es una lista")

most_spoken_languages(countries_data_lst)

