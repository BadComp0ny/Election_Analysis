#The data we nee need to retrieve.
#1. The total number of votes casts.
#2 A list of all candidates that received votes.
#3 The total number of votes each candidate received
#4 the percentage of votes each candidate received
#5 The winner of the election based on the popular vote.

# Add our dependencies
import csv
import os

# Assign a variable for the file to laod and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Create an accumulator
total_votes = 0
# Candidate options and candidate votes
candidate_options = []
candidate_votes = {}

#winning candidate and winning count tracker
winner_candidate = ""
winner_count = 0
winner_percent = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        #2. Add to the total vote count
        total_votes += 1
        
        # Get candidate name from each row
        candidate_name = row[2]
       
        #check to see if candidate name is already in the candidate options:
        if candidate_name not in candidate_options:
            # if not in the list adds the new name to the list
            candidate_options.append(candidate_name)

            #begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        #track votes for each candidate
        candidate_votes[candidate_name] += 1

#Save the results to our text file
with open(file_to_save, "w") as txt_file:
        
    # Print the data to a text file
    election_results = (
        f'\nElection Results\n'
        f'-------------------------\n'
        f'Total Votes: {total_votes:,}\n'
        f'-------------------------\n')
                
    print(election_results, end="")
    #save the final vote count to the text file
    txt_file.write(election_results)


    #calculate total percentage of votes each candidate won
    # go through the candidate list
    for candidate_name in candidate_votes:
            #get the total votes for each candidate
            votes = candidate_votes[candidate_name]
            #calculate the percentage of the vote
            vote_percentage = float(votes) / float(total_votes) * 100
        
            #Print out each candidate's name, vote count, and percentage of votes to the terminal
            #print(f"{candidate_name}: {vote_percentage:.1f}: ({votes:,})\n")

            #Determine winning vote count and candidate
            if (votes > winner_count) and (vote_percentage > winner_percent):
                #if true then set winner_count = votes and winner_percent = vote_percentage
                winner_count = votes
                winner_percent = vote_percentage
                #set winner_candidate = to the candidate's name
                winner_candidate = candidate_name
    winning_candidate_summary = (
        f"--------------------------------\n"
        f'Winner: {winner_candidate}\n'
        f"Winning Vote Count: {winner_count:,}\n"
        f"Winning Percentage: {winner_percent:.1f}\n"
        f"--------------------------------\n")
    #print(winning_candidate_summary)

    #3. Print the total votes   
    #print(total_votes)
    