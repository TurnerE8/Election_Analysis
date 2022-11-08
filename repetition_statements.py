# While Loops
x = 5
while x <= 5: 
    print (x)
    x = x+1

#For Loops
counties = ["Arapahoe", "Denver", "Jefferson"]
for county in counties: 
    print(county)

numbers = [1, 2, 3, 4, 5, 6, 7]
for num in numbers: 
    print(num)

# Looping through Dictionaries 
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties.dict: 
    print(county)

# Getting the Values from a list of Dictionaries 
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data: 
    for value in county_dict.values():
        print(value)