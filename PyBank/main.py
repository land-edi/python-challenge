# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
#Create output directory
saving = os.path.join('..', 'Outputs')
if not os.path.exists(saving):
    os.mkdir(saving)

# Module for reading CSV files
import csv
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

#Get columns in list
str_date = []
revenue = []
change = []
prev_revenue = 0 # to hold the previous revenue value


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
        str_date.append(row[0])
        revenue.append(int(row[1]))
        change.append(int(row[1]) - prev_revenue)
        prev_revenue = int(row[1])

#Average change in profit/losses
change[0] = 0 #Reset the change of the first value to 0
avg_change = sum(change)/(len(change)-1)

#############################
#  Calculation summary data
#############################

#Total number of months
int_total_month = len(str_date)

# Total net Amount of Profit/Losses
total_revenue = sum(revenue)

#Greatest increase in profit
great_increase = max(change)
month_increase = [str_date[i] for i in range(len(str_date)) if change[i] == great_increase]

#Greatest Decrease in profit
great_decrease = min(change)
month_decrease = [str_date[i] for i in range(len(str_date)) if change[i] == great_decrease]

# Print to terminal
print("Financial Analysis\n----------------------------\nTotal Months: {0}\nTotal: ${1}\nAverage  Change: ${2:8.2f}\nGreatest Increase in Profits: {3} (${4})\nGreatest Decrease in Profits: {5} (${6})".format(int_total_month, total_revenue, avg_change, month_increase[0], great_increase, month_decrease[0], great_decrease))

##################################
# Print to output file
##################################
outpath = os.path.join('..', 'Outputs', 'budget_data.txt')
my_file = open(outpath, "w")
print("Financial Analysis\n----------------------------\nTotal Months: {0}\nTotal: ${1}\nAverage  Change: ${2:8.2f}\nGreatest Increase in Profits: {3} (${4})\nGreatest Decrease in Profits: {5} (${6})".format(int_total_month, total_revenue, avg_change, month_increase[0], great_increase, month_decrease[0], great_decrease), file=my_file)