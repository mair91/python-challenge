#import modules
import csv
import os
# Specify the file to write to
pollpath = os.path.join("Resources", "election_data.csv")
#Create variable to count number of votes
#Create lists to return data from candidates, number of votes and percentage of votes
countVotes = 0
cand = []
votesNum = []
votesPerc = []
with open(pollpath, newline = "") as csvfile:
csvreader = csv.reader(csvfile, delimiter = ",")
csv_header = next(csvreader)

for row in csvreader:
    countVotes += 1
    if row[2] not in cand:
        cand.append(row[2])
        index = cand.index(row[2])
        votesNum.append(1)
    else:
        votesNum[cand.index(row[2])] += 1

for row in votesNum:
    calc = round((100*(row/countVotes)))
    votesPerc.append(calc)

winCand = cand[votesNum.index(max(votesNum))]
#print results
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(countVotes))
print("-------------------------")
for x in range(len(cand)):
    print(str(cand[x])+": "+"{:.3%}".format(votesPerc[x]/100)+" ("+str(votesNum[x])+")")
print("-------------------------")
print("Winner: "+ str(winCand))
print("-------------------------")

#write to file
output = open("ElectionResults.txt", "w")
output.write("Election Results"+"\n")
output.write("-------------------------"+"\n")
output.write("Total Votes: " + str(countVotes)+"\n")
output.write("-------------------------"+"\n")
for x in range(len(cand)):
    output.write(str(cand[x])+": "+"{:.3%}".format(votesPerc[x]/100)+" ("+str(votesNum[x])+")"+"\n")
output.write("-------------------------"+"\n")
output.write("Winner: "+ str(winCand)+"\n")
output.write("-------------------------"+"\n")
output.close()
