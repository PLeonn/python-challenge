import os
import csv

numMonths = 0
results = 0
oldRow = 0
newRow = 0
change = 0
sumChg = 0
greatIn = 0
greatInMonth = " "
greatDeMonth = " "
greatDe = 0

csvpath = os.path.join("Resources","budget_data.csv")

with open(csvpath, newline='') as csvfile:

	csvreader = csv.reader(csvfile, delimiter=',')

	csv_header = next(csvreader)

	firstRow = next(csvreader)
	oldRow = int(firstRow[1])
	results += oldRow

	for row in csvreader:
		numMonths += 1
		newRow = int(row[1])
		results += newRow

		change = newRow - oldRow
		sumChg += change

		if newRow > oldRow:
			change = newRow - oldRow
			if change > greatIn:
				greatIn = change
				greatInMonth = row[0]

		if newRow < oldRow:
			change = newRow - oldRow
			if change < greatDe:
				greatDe = change
				greatDeMonth = row[0]
		
		oldRow = newRow

	avgChg = sumChg / numMonths

#For formatting: https://stackoverflow.com/questions/10112614/how-do-i-create-a-multiline-python-string-with-inline-variables
	output = """Financial Analysis
	----------------------------
	This period spans across {numMonths} months
	Here are the profits/losses for this period: ${results}
	The average change across this period is ${avgChg}.
	The greatest increase: {greatInMonth} (${greatIn})
	The greatest decrease: {greatDeMonth} (${greatDe})""".format(numMonths = numMonths + 1,results = results,avgChg = "{:.2f}".format(avgChg),greatInMonth = greatInMonth, greatIn = greatIn, greatDeMonth = greatDeMonth, greatDe = greatDe)
	
	print(output)

	PyBank = open("PyBank.bas","w+")
	PyBank.write(output)
	PyBank.close()