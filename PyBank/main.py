import os
import csv

#budget_csv = os.path.join("..", "Resources", "budget_data.csv")

budget_csv="C:/Users/schre/OneDrive/Documents/GitHub/python-challenge/PyBank/Resources/budget_data.csv"

date=[]
profit=[]
total_months=0
total_profit=0
biggest_up=0

biggest_down=0
avg_profit=0

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #read in header row
    next(csvreader)

    for row in csvreader:
        # Add date
        date.append(row[0])
        total_months+=1
        # Add profit/loss
        profit.append(int(row[1]))
        total_profit+=int(row[1])
        if int(row[1]) > biggest_up:
            biggest_up=int(row[1])
            biggest_up_date=row[0]
        if int(row[1]) < biggest_down:
            biggest_down=int(row[1])
            biggest_down_date=row[0]
for prof in profit:
    avg_profit += prof
avg_profit=avg_profit/len(profit)

print('Financial Analysis')
print('----------------------------')

print('Total Months: ', total_months)

print('Total: ', total_profit)

print('Average Change: ', avg_profit)

print('Greatest Increase in Profits: ', biggest_up_date, biggest_up)

print('Greatest Decrease in Profits: ', biggest_down_date, biggest_down)

file = 'C:/Users/schre/OneDrive/Documents/GitHub/python-challenge/PyBank/Resources/output.txt'

# Open the file in "read" mode ('w') and store the contents in the variable "text"
with open(file, 'w') as text:

    # Print the contents of the text file
    text.write('Financial Analysis')
    text.write('\n')
    text.write('----------------------------')
    
    text.write('\n')
    text.write('Total Months: '+ str(total_months))

    text.write('\n')
    text.write('Total: ' + str(total_profit))

    text.write('\n')
    text.write('Average Change: ' + str(avg_profit))
    
    text.write('\n')
    text.write('Greatest Increase in Profits: '+ str(biggest_up_date)+ " "+str(biggest_up))
    
    text.write('\n')
    text.write('Greatest Decrease in Profits: '+str(biggest_down_date) +" " +str(biggest_down))
