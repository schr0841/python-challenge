import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")

date=[]
profit=[]
total_months=0
total_profit=0
biggest_up=0

biggest_down=0
avg_profit=0
value={}
deltas=[]
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #read in header row
    header=next(csvreader)
    largest_delta=0
    delta=0
    smallest_delta=0
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
        if len(profit)>1:
            delta=profit[len(profit)-1]-profit[len(profit)-2]
            value[row[0]]=delta
            deltas.append(delta)
        if largest_delta < abs(delta):
            largest_delta=abs(delta)
            largest_delta_date=row[0]
        if smallest_delta>delta:
            smallest_delta=delta
            smallest_delta_date=row[0]
#print('largest delta: ', largest_delta, 'largest delta date: ', largest_delta_date)
#print('\n')
#print('smallest delta: ', smallest_delta, 'smallest delta date: ', smallest_delta_date)  
#for prof in profit:
#    avg_profit += prof
#avg_profit=avg_profit/len(profit)
total=0
for p in deltas:
    total+=p
#rint('total: ', total/len(deltas))
#print('value: ', value)

max(value)

print('Financial Analysis')
print('----------------------------')

print('Total Months: ', total_months)

print('Total: ', total_profit)

avg_change=total/len(deltas)

print('Average Change: ', "${:,.2f}".format(avg_change))

print('Greatest Increase in Profits: ', largest_delta_date,"${:,.2f}".format(largest_delta))

print('Greatest Decrease in Profits: ', smallest_delta_date, "${:,.2f}".format(smallest_delta))

#file = 'C:/Users/schre/OneDrive/Documents/GitHub/python-challenge/PyBank/Resources/output.txt'
file='Resources/output.txt'
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
    text.write('Average Change: ' + "${:,.2f}".format(avg_change))
    
    text.write('\n')
    text.write('Greatest Increase in Profits: '+ str(largest_delta_date)+ " "+"${:,.2f}".format(largest_delta))
    
    text.write('\n')
    text.write('Greatest Decrease in Profits: '+str(smallest_delta_date) +" " +"${:,.2f}".format(smallest_delta))
