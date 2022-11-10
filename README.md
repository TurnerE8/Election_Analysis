# Election_Analysis

## Project Overview 
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election. 

1. Calculate the total number of votes cast. 
2. Get a complete list of candidates who received votes. 
3. Calculate the total number of votes each candidate received. 
4. Calculate the percentage of votes each candidate won. 
5. Determine the county votes for each county and which county received the highest turnout. 
5. Determine the winner of the election based on popular vote. 

## Resources 
- Data Source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code, 1.38.1 

## Election Audit Results Audit 
The total votes cast in this election was 369,711 votes. The votes came from a total of three counties (Arapahoe, Denver and Jefferson counties). The breakdown of the county votes is as follows: 
1. Arapahoe 
  - 6.7% (24, 801)
2. Jefferson 
  - 10.5% (38, 855)
3. Denver 
  - 82.8% (306, 055)
  
The county with the largest voter turnout was Denver. 

The number of candidates participating in this election was a total of three. The breakdown of the candidate votes is as follows: 
1. Raymon Doane 3.1% (11,606)
2. Charles Stockham 23.0% (85, 213)
3. Diana DeGette 73.8% (272, 892) 
The candidate who received the most votes, by quite a large margin, was Diana DeGette. 

For a faster view of the election results, please see the election_results.txt text file saved in the repository. 

## Election Audit Summary 
The advantage of establishing this script is that it can be applied to future election audits. Most of the work will be done by simply ensuring your analyzing the correct CSV file and you have established the correct path to said file. The variables and their names may need to be tweaked based on election specifics (i.e. county names, number of counties, candidates, etc.), however, most of the work will already be done for you once you give the new set of data a quick overview before applying the new data and runnning the script. 
Where I struggled initially with the script was establishing the variables for the various decision statements and when iterating through the rows of data. I received error after error because some of my variables were not defined. Additionally, working with the 'f' strings proved challenging and I struggled with getting the correct syntax. I matched up much of what was learned throughout the module and that seemed to help. 
