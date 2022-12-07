from countries import countries

for data in countries:
    contain_land = "land" in data
    if contain_land == True:
        print(data)
