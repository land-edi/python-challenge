# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv
csvpath = os.path.join('..', 'Resources', 'election_data.csv')

#Get columns in list
voter = []
county = []
candidate_vote = []


################################################
#Reading the CSV and performing calculations
################################################

with open(csvpath, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # Read each row of data after the header and performs calculation
    for row in csvreader:
        voter.append(row[0])
        county.append(row[1])
        candidate_vote.append(row[2])

# Get the list of candidates
candidate_list = list(set(candidate_vote))

################################
#Get stats for each candidate
################################
results = []
total_vote = len(candidate_vote)
for candidate in candidate_list:
    votes = len([value for value in candidate_vote if value == candidate])
    percentage = (votes/total_vote)*100.0
    results.append((candidate, percentage, votes))

#Sort the list using the candidates' votes in descending order
results.sort(reverse=True, key=lambda x:x[2])

######################################
#Print the results
######################################
print(f"Election Results\n-------------------------\nTotal Votes: {total_vote}\n-------------------------")
for candidate,perct,vote in results:
    print("{0}: {1:2.3f}% ({2})".format(candidate, perct, vote))
print(f"-------------------------\nWinner: {results[0][0]}\n-------------------------")

##################################
# Print to output file
##################################
outpath = os.path.join('..', 'Outputs', 'election_data.txt')
my_file = open(outpath, "w")

print(f"Election Results\n-------------------------\nTotal Votes: {total_vote}\n-------------------------", file=my_file)
for candidate,perct,vote in results:
    print("{0}: {1:2.3f}% ({2})".format(candidate, perct, vote), file=my_file)
print(f"-------------------------\nWinner: {results[0][0]}\n-------------------------", file=my_file)
