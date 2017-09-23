def substringcounter(substrings, string,caseSensitive = False):

	if  caseSensitive == False:
		string = string.lower()
		substrings = set(map(str.lower,substrings))
	counts = dict.fromkeys(substrings,0)
	for i in substrings:
		for j in string.split(" "):
			if i in j:
				counts[i] += 1
	return counts
