# We saved the results of the watson computations in a semicolon-separated csv file, which became problematic when headlines and URLs contained semicolons aswell.
# This program fixes the formating by replacing the separating semicolons with char(30), an ASCII separation character.

with open("articleMood_copy.csv", "r") as inFile:
	with open("articleMoodCorrected.csv", "w") as outFile:
		for line in inFile:

			newLine = line
			if newLine.count(";") == 9:
				newLine = newLine.replace(";",chr(30)) # record separation symbol. this >should< not occur in any text ever
			else:
				# replace the delimiter between id and headline
				left = newLine.find(";")
				newLine = newLine[:left]+chr(30)+newLine[left+1:]
				right = -1
				# replace the delimiters between the five emotions, timestamp, publisher and url
				for i in range(7):
					right = newLine.rfind(";")
					newLine = newLine[:right]+chr(30)+newLine[right+1:]

				# find the missing separating ;
				# we have to iterate from the right, since the order in the file goes 'headline;URL' and some websites have their URL as their headline too
				while True:
					right = newLine.rfind(";", left, right)
					# if we found the separating ; we can replace it and leave the others be
					if newLine[right+1:right+8] == "http://" or newLine[right+1:right+9] == "https://":
		                                newLine = newLine[:right]+chr(30)+newLine[right+1:]
						break
					# else we just move on, since that ; is important for the URL
					else:
						right -= 1


					if right <0:
						print(line+"\n")
						print(newLine+"\n\n")
						break

			outFile.write(newLine)
