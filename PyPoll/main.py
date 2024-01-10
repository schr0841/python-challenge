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

biggest_down=0
avg_profit=0

with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #read in header row
    next(csvreader)

    for row in csvreader:
        # Add date
        candidate[row[0]]=+1

for c in candidate.keys():
    print(f'Candidate ', candidate[c])