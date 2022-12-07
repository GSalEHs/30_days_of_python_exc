from countries_data import countries_data_lst


total_languages=0
total_lan_values=[]
number_rep_lan_lst=[]
countrie_name_key_lst = []
population_value_lst = []
for person_dict in countries_data_lst:
    data_index = countries_data_lst.index(person_dict)
    ind_data = countries_data_lst[data_index]
    number_languages = len(ind_data["languages"])
    total_languages+=number_languages
    for lan_value in ind_data["languages"]:
        total_lan_values.append(lan_value)
for ind_lan_value in total_lan_values:
    number_rep_lan = total_lan_values.count(ind_lan_value)
    number_rep_lan_lst.append(number_rep_lan)
for name_key in countries_data_lst:
    name_key_value = name_key["name"]
    countrie_name_key_lst.append(name_key_value)
for population_key in countries_data_lst:
    population_key_value = population_key["population"]
    population_value_lst.append(population_key_value)


countrie_total_dict = dict.fromkeys(countrie_name_key_lst)
lang_total_dict = dict.fromkeys(total_lan_values)

countrie_total_dict.update(zip(countrie_total_dict, population_value_lst))
lang_total_dict.update(zip(lang_total_dict, number_rep_lan_lst))

from operator import itemgetter
lang_sorted_tuple = sorted(lang_total_dict.items(), key=itemgetter(1), reverse=True)

ten_more_items = dict(lang_sorted_tuple[0: 10])

countrie_sorted_tuple = sorted(countrie_total_dict.items(), key=itemgetter(1), reverse=True)

ten_most_populated = dict(countrie_sorted_tuple[0: 10]).keys()


print(f"the 10 most populated countries in the world are: {ten_most_populated}")
print(f"the 10 most spoken languages are: {ten_more_items}")
print(f"total languages in the database are: {total_languages} ")
different_languages = set(total_lan_values)
different_languages_number = len(different_languages)
print(f"total different languages: {different_languages_number}")
