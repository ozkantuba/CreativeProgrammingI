nouns = []	
											# create an empty list
with open('WordLists/SingularNouns.txt') as word_file:	# open the file's contents
	for line in word_file:								# iterate through all lines in the file
		word = line.strip()								# remove newline (\n) characters
		nouns.append(word)
										# add to list of words!
print nouns[0:20]	