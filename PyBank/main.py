#import modules
import csv
import os

# Specify the file to write to
budgetpath = os.path.join("Resources", "budget_data.csv")

# Open the file. Specify the variable to hold the contents
with open(budgetpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvfile)

    ProfitLoss = []
    Periods = []
    Variation = []
    
#read each row of file
    for rows in csvreader:
        ProfitLoss.append(int(rows[1]))
        Periods.append(rows[0])

    for x in range(1, len(ProfitLoss)):
        Variation.append((int(ProfitLoss[x]) - int(ProfitLoss[x-1])))
    
#calculate average revenue
    AveRevenue = sum(Variation) / len(Variation)
    
#calculate number of months in data
    Months = len(Periods)

#find greatest increase in profits
    GrtIncrease = max(Variation)

#find greatest decrease in profits
    GrtDecrease = min(Variation)

#print stats
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(Months))
    print("Total: $" + str(sum(ProfitLoss)))
    print("Average  Change: $" + str("{:.2f}".format(AveRevenue)))
    print("Greatest Increase in Profits: " + str(Periods[Variation.index(max(Variation))+1]) + " " + '$(' + str(GrtIncrease) + ')')
    print("Greatest Decrease in Profits: " + str(Periods[Variation.index(min(Variation))+1]) + " " + '$(' + str(GrtDecrease) + ')')

#write to file
    output = open("Analysis/ProfitLossResults.txt", "w")
    output.write("Financial Analysis"+"\n")
    output.write("----------------------------"+"\n")
    output.write("Total Months: " + str(Months)+"\n")
    output.write("Total: $" + str(sum(ProfitLoss))+"\n")
    output.write("Average  Change: $" + str("{:.2f}".format(AveRevenue))+"\n")
    output.write("Greatest Increase in Profits: " + str(Periods[Variation.index(max(Variation))+1]) + " " + '$(' + str(GrtIncrease) + ')'+"\n")
    output.write("Greatest Decrease in Profits: " + str(Periods[Variation.index(min(Variation))+1]) + " " + '$(' + str(GrtDecrease) + ')'+"\n")
    output.close()
