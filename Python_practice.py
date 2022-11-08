


# Using IF statements
#counties = ["Arapahoe", "Denver", "Jefferson"]
#If counties[1]== "Denver': 
# print(counties[1])

#If counties[3] != "Jefferson"
#    print(counties[2])

# Using IF-ELSE statements
#temperature = int(input("What is the temperature outside?"))

#If temperature >80
    #print("Turn on the AC.")
#Else 
    #print("Open the window.")

#What is the score?
#score = int(input("What is your test score? "))

# Determine the grade.
#if score >= 90:
    #print('Your grade is an A.')
#else:
    #if score >= 80:
     #   print('Your grade is a B.')
    #else:
     #   if score >= 70:
      #      print('Your grade is a C.')
       #    if score >= 60:
        #        print('Your grade is a D.')
         #   else:
          #      print('Your grade is an F.')    

# What is the score?
#score = int(input("What is your test score? "))

# Determine the grade.
#if score >= 90:
    #print('Your grade is an A.')
#elif score >= 80:
    #print('Your grade is a B.')
#elif score >= 70:
    #print('Your grade is a C.')
#elif score >= 60:
    #print('Your grade is a D.')
#else:
    #print('Your grade is an F.')

# Membership operators creation 
counties = ["Arapahoe", "Denver", "Jefferson"]
if "El Paso" in counties : 
    print("El Paso is in the list of counties.")
else: 
    print("El Paso is not in the list of counties.")

# Logical operators creation
if "Arapahoe" in counties and "El Paso" in counties : 
    print("Arapahoe and El Paso are in the list of counties.")
else: 
    print("Ararahoe or El Paso is not in the list of counties")

# F-STRINGS 
    # Original code below: 
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")
    # Edited using F String literal 
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")



