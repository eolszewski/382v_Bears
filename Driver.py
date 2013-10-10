import math
# Open a file
bearArray = [line.strip() for line in open("Input.txt")]

def makeBears( bearArray ):	
	formattedBearArray = []
	for bear in bearArray:
		bearParts = bear.lower().split(' : ')
		formattedBearArray.append(bearParts)
	return formattedBearArray

formattedBearArray = makeBears(bearArray)

for selectedBearIndex in range(0, len(formattedBearArray)):
	for possibleMatchIndex in range(selectedBearIndex+1, len(formattedBearArray)):
		if (formattedBearArray[selectedBearIndex][1] != formattedBearArray[possibleMatchIndex][1]
			and float(formattedBearArray[selectedBearIndex][4]) <= 6.0 
			and float(formattedBearArray[selectedBearIndex][4]) >= 2.0
			and float(formattedBearArray[possibleMatchIndex][4]) <= 6.0 
			and float(formattedBearArray[possibleMatchIndex][4]) >= 2.0 
			and math.fabs(float(formattedBearArray[selectedBearIndex][4]) - float(formattedBearArray[possibleMatchIndex][4])) <= 1.0):
			selectedRelatives = [];
			selectedRelatives.append(formattedBearArray[selectedBearIndex][2])
			selectedRelatives.append(formattedBearArray[selectedBearIndex][3])
			matchRelatives = [];
			matchRelatives.append(formattedBearArray[possibleMatchIndex][2])
			matchRelatives.append(formattedBearArray[possibleMatchIndex][3])
			for selectedRelativeIndex in range(0, len(formattedBearArray)):
				if (formattedBearArray[selectedRelativeIndex][0] == selectedRelatives[0] or formattedBearArray[selectedRelativeIndex][0] == selectedRelatives[1]):
					selectedRelatives.append(formattedBearArray[selectedRelativeIndex][2]) 
					selectedRelatives.append(formattedBearArray[selectedRelativeIndex][3]) 
				if (formattedBearArray[selectedRelativeIndex][0] == matchRelatives[0] or formattedBearArray[selectedRelativeIndex][0] == matchRelatives[1]):
					matchRelatives.append(formattedBearArray[selectedRelativeIndex][2]) 
					matchRelatives.append(formattedBearArray[selectedRelativeIndex][3]) 
			if(len(set(matchRelatives) & set(selectedRelatives)) == 0):
				strs = ""
				for selectedParentIndex in range(0, len(formattedBearArray)):
					if (formattedBearArray[selectedBearIndex][0] == formattedBearArray[selectedParentIndex][2] or 
						formattedBearArray[selectedBearIndex][0] == formattedBearArray[selectedParentIndex][3] or 
						formattedBearArray[possibleMatchIndex][0] == formattedBearArray[selectedParentIndex][2] or 
						formattedBearArray[possibleMatchIndex][0] == formattedBearArray[selectedParentIndex][3]):
						strs = "false"
				if strs != "false":
					strs = bearArray[selectedBearIndex].split(' : ')[0] + " + " + bearArray[possibleMatchIndex].split(' : ')[0]
					print strs
