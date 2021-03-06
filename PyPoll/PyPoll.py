import os
import csv
import operator 
from collections import defaultdict


# Path to collect data from Resources folder
csvpath = os.path.join('.', 'PyPoll', 'Resources', 'election_data.csv')
#csvpath= os.path.join("Resources/election_data.csv")

# Define Variables 
total_votes = 0 
candidate_votes = {}
candidate_votes_percentage = {}
combined_votes_percentages = defaultdict(list)
candidates = []
percentage = 0 
winner_name = []


# Read is csv file
with open(csvpath) as csvfile:

    # Split the data on commas 
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # Loop through the rows of data 
    for row in csvreader:

        # Calculate the total number of votes cast 
        total_votes = total_votes + 1

        name = row[2]

        # Calculate the total number of votes each candidate won 
        if name not in candidate_votes:
            candidate_votes[name] = 1
        else:
            if candidate_votes[name] == 1:
                candidates.append(name)
                candidate_votes[name] += 1 
            else:
                candidate_votes[name] += 1
   
# Calculate the percentage of votes each candidate won and create a new dictionary with candidate name and votes with same values from candidate_votes
candidate_votes_percentage = dict(candidate_votes)  

vote_res = ""
for key, value in candidate_votes_percentage.items():
    
    vote_percentage = float (value)/float(total_votes) * 100
    vote_res += key + ' '+ f'{vote_percentage:.3f}%  ({value})\n'

# Determine the winner of the election based on the poplar vote 
winner_name = max(candidate_votes.items(), key=operator.itemgetter(1))[0]


# Set format for printing 
output = (
    f"Election Results\n"
    f"-----------------\n"
    f"Total Votes: {total_votes} \n"
    f"-----------------\n"
    f"{vote_res} \n"
    f"-----------------\n"
    f"Winner: {winner_name}\n"
    f"-----------------"
)

print(output)

with open("analysis/output.txt", "w") as txt_file: 
    txt_file.write(output)