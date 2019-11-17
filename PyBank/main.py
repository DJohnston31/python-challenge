# Import the os module as well as the csv module for reading csv files. This will allow us to create file paths across operating systems and read csv files

import os
import csv

csvpath = os.path.join('Budget_Data.csv')

# Create Lists to store data

Monthlist = []
PLlist = []

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
        Monthlist.append(row[0])
        PLlist.append(float(row[1]))

# Print Title named Financial Analysis
print("Financial Analysis")
print("----------------------------------")

# Create a variable for Total number of months included in the dataset

Total_Months = len(Monthlist)
# print(Total_Months)


# Create a variable for the net total amount of "Profit/Losses" over the entire period

Total = sum(PLlist)
# print(Total)

# Create a variable for the average of the changes in "Profit/Losses" over the entire period

Average_Change = sum(PLlist) / len(PLlist) 
# print(Average_Change)

# Create a variable for the greatest increase in profits (date and amount) over the entire period

Greatest_Increase_Amount = max(PLlist)
# print(Greatest_Increase_Amount)

#Identify the index of the variable for the greatest increase in profits
# print(PLlist.index(Greatest_Increase_Amount))

IndexBestProfit = PLlist.index(Greatest_Increase_Amount)
Greatest_Increase_Date = Monthlist[IndexBestProfit]
# print(Greatest_Increase_Date)

# Create a variable for the greatest decrease in losses (date and amount) over the entire period

Greatest_Decrease_Amount = min(PLlist)
# print(Greatest_Decrease_Amount)

#Identify the index of the variable for the greatest decrease in profits
# print(PLlist.index(Greatest_Decrease_Amount))

IndexWorstProfit = PLlist.index(Greatest_Decrease_Amount)
Greatest_Decrease_Date = Monthlist[IndexWorstProfit]
# print(Greatest_Decrease_Date)

# Print the analysis to the terminal

# Print a statement adding the Total Months
print("Total Months: " + str(Total_Months)) 

# Prints a statement adding the Total 
print("Total: " + str(Total))

# Print the Average Change
print("Average Change: " + str(Average_Change))

# Print the Greatest Increase in Profits
print("Greatest Increase in Profits: " + str(Greatest_Increase_Date) + "(" + str(Greatest_Increase_Amount) + ")")

# Print the Greatest Decrease in Profits
print("Greatest Decrease in Profits: " + str(Greatest_Decrease_Date) + "(" + str(Greatest_Decrease_Amount) + ")")

# # Export a text file with the results.

# # Specify the file to write to
# output_path = os.path.join("..", "output", "new.csv")

# # Open the file using "write" mode. Specify the variable to hold the contents
# with open(output_path, 'w', newline='') as csvfile:

#     # Initialize csv.writer
#     csvwriter = csv.writer(csvfile, delimiter=',')

#     # Write the first row (column headers)
#     csvwriter.writerow(['First Name', 'Last Name', 'SSN'])