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


#GETTING TOTAL VOTE COUNTS 3.5.1 and on for code 
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

# Candidate Options
candidate_options = []

# Declare an empty dictionary so we can begin getting votes for each candidate
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    # Read the file object with the reader function 
    file_reader = csv.reader(election_data) 

    # Read and print the header row
    headers = next(file_reader)
    # Print each row in the CSV file
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1

            # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            # After creating empty dictionary above, set the values inside dict to zero so we can start counting votes
            candidate_votes[candidate_name] = 0

        # Add a vote to the candidates count
        candidate_votes[candidate_name] += 1

# Save the results to our text file
with open(file_to_save, "w") as txt_file: 

    #Print the final vote count to the terminal 
    election_results = (
        f"\nElection Results\n"
        f"-----------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-----------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file. 
    txt_file.write(election_results)

    # Determine the % of votes for each candidate by looping through the counts
    # Iterate through candidate list
    for candidate_name in candidate_votes: 
        #Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        #Calculate the percentage of the vote
        vote_percentage = float(votes) / float(total_votes)*100
        # Print each candidate, their voter count, and percentage to the
        # terminal.
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
        # Print each candidates voter count and percentage to the terminal
        print(candidate_results)
        # Save the candidate results to our text file. 
        txt_file.write(candidate_results)

        # To do: print each candidates name, vote count and percentage to the terminal 
        # Determine winning vote count and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

    #  To do: print out the winning candidate, vote count and percentage to
    #   terminal.

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    print(winning_candidate_summary)
    # Save the winning candidates results to the text file
    txt_file.write(winning_candidate_summary)