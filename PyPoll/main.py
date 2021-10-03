import os
import csv

# Define Variables
total_number_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
tooley_votes = 0

#soruce CSV file
csv_path = os.path.join('.', 'PyPoll', 'Resources', 'election_data.csv')

#Open and Read the csv file
with open(csv_path, newline ='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)
    #row = next(csvreader)
    
    #Calculate TOtal number of votes for each candidates won.
    for row in csvreader:
        total_number_votes +=1
        if (row[2] == "Khan"):
            khan_votes += 1
        elif (row[0] == "Correy"):
            correy_votes = 0
        elif (row[0] == "Li"):
            li_votes += 1
        else:
            tooley_votes += 1

#Calculate percentage of votes each candiate won
khan_percent = khan_votes / total_number_votes
correy_percent = correy_votes / total_number_votes
li_percent = li_votes / total_number_votes
tooley_percent = tooley_votes / total_number_votes
candidate_winner = max(khan_votes, correy_votes, li_votes,tooley_votes)
if candidate_winner == khan_votes:
    winner = "Khan"
elif candidate_winner == correy_votes:
    winner = "Correy"
elif candidate_winner == li_votes:
    winner = "Li"
else:
    winner = "O'Tooley"

#Print the details as requested
print(f"Election Results")
print(f"---------------------------")
print(f"Total Votes: {total_number_votes}")
print(f"---------------------------")
print(f"Kahn: {khan_percent:.3%}({khan_votes})")
print(f"Correy: {correy_percent:.3%}({correy_votes})")
print(f"Li: {li_percent:.3%}({li_votes})")
print(f"O'Tooley: {tooley_percent:.3%}({tooley_votes})")
print(f"---------------------------")
print(f"Winner: {candidate_winner}")
print(f"---------------------------")

# Path to the output of the file.
output_file = os.path.join('.', 'PyPoll', 'Election_Data_Revised.text')

# Using "Write" Mode. 
with open(output_file, 'w',) as txtfile:

# write data to the textfile
    txtfile.write(f"Election Results\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Votes: {total_number_votes}\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Kahn: {khan_percent:.3%}({khan_votes})\n")
    txtfile.write(f"Correy: {correy_percent:.3%}({correy_votes})\n")
    txtfile.write(f"Li: {li_percent:.3%}({li_votes})\n")
    txtfile.write(f"O'Tooley: {tooley_percent:.3%}({tooley_votes})\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Winner: {candidate_winner}\n")
    txtfile.write(f"---------------------------\n")