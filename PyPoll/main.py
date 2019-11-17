# Import the os module as well as the csv module for reading csv files. This will allow us to create file paths across operating systems and read csv files

import os
import csv

csvpath = os.path.join('Election_Data.csv')

# Create Lists to store data

VoterIDList = []
CountyList = []
CandidateList = []
UniqueCandidateList = []

#Improved Reading using CSV module

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)

    # Read the header row first
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    #Read each row of data after the header and add to lists

    for row in csvreader:
        VoterIDList.append(float(row[0]))
        CountyList.append(row[1])
        CandidateList.append(row[2])

# Establish the unique list of Candidates from improved Reading using CSV module

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)

    # Read the header row first
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    for Candidates in CandidateList:
        if Candidates not in UniqueCandidateList:
            UniqueCandidateList.append(Candidates)

# print(UniqueCandidateList)

# Create a variable for Total number of months of votes cast from the dataset

Total_Votes = len(VoterIDList)
# print(Total_Votes)

# Create variables for each of the candidates total votes
KhanVoterIDList = []
CorreyVoterIDList = []
LiVoterIDList = []
OTooleyVoterIDList = []

Khan = UniqueCandidateList[0]
Correy = UniqueCandidateList[1]
Li = UniqueCandidateList[2]
OTooley = UniqueCandidateList[3]

# Loop through the data to assign list of VoterIDs associated with each of the respective candidates 
    
#Improved Reading using CSV module

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)

    # Read the header row first
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    #Read each row of data after the header and add to lists
        
    for row in csvreader:
        if row[2] == OTooley:
            OTooleyVoterIDList.append(float(row[0]))
        elif row[2] == Li:
            LiVoterIDList.append(float(row[0]))
        elif row[2] == Correy:
            CorreyVoterIDList.append(float(row[0]))
        else:
            KhanVoterIDList.append(float(row[0]))

# Create a variable for Total number of votes for each candidate cast from the dataset

OTooleyTotal_Votes = len(OTooleyVoterIDList)
LiTotal_Votes = len(LiVoterIDList)
CorreyTotal_Votes = len(CorreyVoterIDList)
KhanTotal_Votes = len(KhanVoterIDList)

# print(OTooleyTotal_Votes)
# print(LiTotal_Votes)
# print(CorreyTotal_Votes)
# print(KhanTotal_Votes)

# Create a variable for % of Total votes for each candidate cast from the dataset

PctVotesOTooleyWon = int((OTooleyTotal_Votes / Total_Votes) * 100)
PctVotesLiWon = int((LiTotal_Votes / Total_Votes) * 100)
PctVotesCorreyWon = int((CorreyTotal_Votes / Total_Votes) * 100)
PctVotesKhanWon = int((KhanTotal_Votes / Total_Votes) * 100)

# print(PctVotesOTooleyWon)
# print(PctVotesLiWon)
# print(PctVotesCorreyWon)
# print(PctVotesKhanWon)

# Determine the winner of the election based on popular vote

if PctVotesOTooleyWon > PctVotesLiWon and PctVotesOTooleyWon > PctVotesCorreyWon and PctVotesOTooleyWon > PctVotesKhanWon:
    winner = OTooley
elif PctVotesLiWon > PctVotesOTooleyWon and PctVotesLiWon > PctVotesCorreyWon and PctVotesLiWon > PctVotesKhanWon:
    winner = Li
elif PctVotesCorreyWon > PctVotesOTooleyWon and PctVotesCorreyWon > PctVotesLiWon and PctVotesCorreyWon > PctVotesKhanWon:
    winner = Correy
elif PctVotesKhanWon > PctVotesOTooleyWon and PctVotesKhanWon > PctVotesLiWon and PctVotesKhanWon > PctVotesCorreyWon:
    winner = Khan

# print(winner)


# # Print the analysis to the terminal

# Print Title named Election Results
print("Election Results")
print("----------------------------------")

# Print a statement of the Total Votes
print("Total Votes: " + str(Total_Votes)) 

# Print statements of each candidate along with both the associated % of Total Votes and Total Votes
print("Khan: " + str(PctVotesKhanWon) +"% " + "(" + str(KhanTotal_Votes) + ")")
print("Correy: " + str(PctVotesCorreyWon) +"% " + "(" + str(CorreyTotal_Votes) + ")")
print("Li: " + str(PctVotesLiWon) +"% " + "(" + str(LiTotal_Votes) + ")")
print("O'Tooley: " + str(PctVotesOTooleyWon) +"% " + "(" + str(OTooleyTotal_Votes) + ")")

# Prints a statement announcing the winner
print("Winner: " + str(winner))

# Export a text file with the results.

# Specify the file to write to
output_path = os.path.join('new.csv')

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as newcsvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(newcsvfile, delimiter=',')

    # Write the first row
    csvwriter.writerow(['Election', 'Results'])

    # Write the nex rows
    csvwriter.writerow(['Total Votes', str(Total_Votes)])
    csvwriter.writerow(['Khan', str(PctVotesKhanWon) + '%', str(KhanTotal_Votes)])
    csvwriter.writerow(['Correy', str(PctVotesCorreyWon) + '%', str(CorreyTotal_Votes)])
    csvwriter.writerow(['Li', str(PctVotesLiWon) + '%', str(LiTotal_Votes)])
    csvwriter.writerow(['OTooley', str(PctVotesOTooleyWon) + '%', str(OTooleyTotal_Votes)])
    csvwriter.writerow(['Winner', winner])