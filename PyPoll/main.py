import os
import csv

#budget_csv = os.path.join("..", "Resources", "budget_data.csv")


election_csv = os.path.join("Resources","election_data.csv")
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
    header=next(csvreader)

    for row in csvreader:
        if candidate.get(row[2])==None:
            candidate[row[2]]=1
        else: candidate[row[2]]+=1
        total_votes+=1


file = 'analysis/output.txt'


# Open the file in "write" mode ('w') and store the contents in the variable "text"
with open(file, 'w') as text:

    # Print the contents of the text file
    text.write('Election Results')
    text.write('\n')
    text.write('----------------------------')
    
    print("Election Results")
    print('----------------------------')

    text.write('\n')
    text.write('Total votes: '+ str(total_votes))
    print('Total votes: '+ str(total_votes))
    print('----------------------------')
    text.write('\n')
    text.write('----------------------------')
    text.write('Total: ' + str(total_profit))

#print(f"{prob:.2%}")
    
    for item in candidate.keys():
        print(item, f"{candidate[item]/total_votes:.3%}", f"({candidate[item]})" )
        text.write('\n')
        text.write(str(item)+" " +f"{candidate[item]/total_votes:.3%}"   +" "+f"({candidate[item]})")
        text.write('\n')
    winner = max(candidate,key=candidate.get)
    text.write('\n')
    text.write('----------------------------')
    print('----------------------------')

    print("Winner: ", winner)
    text.write('\n')
    text.write("Winner: " + str(winner))

    text.write('\n')
    text.write('----------------------------')
    print('----------------------------')
    
    #text.write('Average Change: ' + str(avg_profit))
    
    