# The data we need to retrieve 
#1. The total number of votes cast 
#2. Complete list of candidates who received votes
#3. The percentage of votes each candidate received
#4. The total number of votes each candidate received
#5. The winner of the election based on popular vote


# Assign a variable for the file to load and the path 
#file_to_load = 'Resources\election_results.csv'
# Open the election_results and read the file
#with open(file_to_load) as election_data: 
    # to do: Perform analysis
    #print(election_data)

# WRITING TO FILES WITH PYTHON 
# Create a filename variable to a direct or indirect path to the file.
#import os
#file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
#open(file_to_save, "w")

####the above steps creatde the election_analysis.txt file in the analysis folder

# WRITING TO FILES WITH PYTHON CONTINUED...
# Use the open statement to open the file as a text file
#outfile = open(file_to_save, "w")
#write data to the file - this will print "hello world" into the election_analysis.txt file
#outfile.write("Hello World")
#close the file
#outfile.close()

#instead of using the open and close statements all of the time, we use a with statement. see below
# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    #txt_file.write("Hello World")

    ###NOW, WRITE THE THREE COUNTIES TO THE election_analysis file
        # Write three counties to the file.
     #txt_file.write("Arapahoe, Denver, Jefferson")
#SKILL DRILL FOR 3.4.3
    #txt_file.write("Counties in the Election\n------------\nArapahoe\nDenver\nJefferson")
    #USING THE "N" newline escape sequence, that puts them all in different lines(refer to election analysis file)

#3.4.4 Reading the Election Results
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    # Read the file object with the reader function 
    file_reader = csv.reader(election_data) 

    # Read and print the header row
    headers = next(file_reader)
    print(headers)