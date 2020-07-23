import os
import csv

totalVotes = 0
candidates = []
votes = []
winner = ""

csvpath = os.path.join("Resources","election_data.csv")

with open(csvpath, newline='') as csvfile:

	csvreader = csv.reader(csvfile, delimiter=',')

	csv_header = next(csvreader)


	for row in csvreader:
		totalVotes += 1
		
		if row[2] not in candidates:
			candidates.append(row[2])
		
		#Help tracking indicies https://stackoverflow.com/questions/7233575/what-is-the-proper-way-to-track-indexes-in-python
		for index, candidate in enumerate(candidates):
			if row[2] == candidate:

				if len(votes) < len(candidates):
					votes.append(int(1))
				
				else:
					votes[index] += 1

			if votes[index] >= max(votes):
				winner = candidates[index]

output = """Election Results
-------------------------
Total Votes: {totalVotes}
-------------------------\n""".format(totalVotes = totalVotes)

for i in range(len(candidates)):
	percentage = 100*votes[i]/totalVotes
	output += candidates[i] + ": " + "{:.3f}".format(percentage) + "% (" + str(votes[i]) + ")\n"

output += """
-------------------------
Winner : """ + winner + "\n-------------------------"

PyPoll = open("PyPoll.bas","w+")
PyPoll.write(output)
PyPoll.close()