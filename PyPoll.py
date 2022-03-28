#The data we nee need to retrieve.
#1. The total number of votes casts.
#2 A list of all candidates that received votes.
#3 The total number of votes each candidate received
#4 the percentage of votes each candidate received
#5 The winner of the election based on the popular vote.
import csv
import os
#Assign a variable for the file to laod and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    #To Do: Read and analyze the data here.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)
    