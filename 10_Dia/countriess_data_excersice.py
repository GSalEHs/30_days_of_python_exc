from countries_data import countries_data_lst


total_languages=0
total_lan_values=[]
number_rep_lan_lst=[]
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


lang_total_dict = dict.fromkeys(total_lan_values)

lang_total_dict.update(zip(lang_total_dict, number_rep_lan_lst))

from operator import itemgetter
lang_sorted_tuple = sorted(lang_total_dict.items(), key=itemgetter(1), reverse=True)

ten_more_items = dict(lang_sorted_tuple[0: 10])

print(f"the 10 most spoken languages are: {ten_more_items}")
print(f"total languages in the database are: {total_languages} ")
different_languages = set(total_lan_values)
different_languages_number = len(different_languages)
print(f"total different languages: {different_languages_number}")


