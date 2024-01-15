import os
import csv

#budget_csv = os.path.join("..", "Resources", "budget_data.csv")

election_csv="C:/Users/schre/OneDrive/Documents/GitHub/python-challenge/PyPoll/Resources/election_data.csv"

id=[]
county=[]
candidate={}
total_months=0
total_profit=0
biggest_up=0
total_votes=0

with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #read in header row
    next(csvreader)

    for row in csvreader:
        # Add date
        #print(candidate.get(row[2]))
        #candidate[row[2]]=1
        #print(row[2])
        if candidate.get(row[2])==None:
            candidate[row[2]]=1
        else: candidate[row[2]]+=1
        total_votes+=1


file = 'C:/Users/schre/OneDrive/Documents/GitHub/python-challenge/PyPoll/Resources/output.txt'

# Open the file in "write" mode ('w') and store the contents in the variable "text"
with open(file, 'w') as text:

    # Print the contents of the text file
    text.write('Election Results')
    text.write('\n')
    text.write('----------------------------')
    
    text.write('\n')
    text.write('Total votes: '+ str(total_votes))
    print('Total votes: '+ str(total_votes))
    text.write('\n')
    text.write('----------------------------')
    #text.write('Total: ' + str(total_profit))


    for item in candidate.keys():
        print(item, candidate[item]/total_votes*100, candidate[item])
        text.write('\n')
        text.write(str(item)+" " +str(candidate[item]/total_votes*100)+" "+str(candidate[item]))
        text.write('\n')
    winner = max(candidate,key=candidate.get)
    text.write('\n')
    text.write('----------------------------')
    print("Winner: ", winner)
    text.write('\n')
    text.write("Winner: " + str(winner))

    text.write('\n')
    text.write('----------------------------')
    #text.write('Average Change: ' + str(avg_profit))
    
    