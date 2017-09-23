 def substringcounter(substrings, string,caseSensitive = False):

	if  caseSensitive == False:
		string = string.lower()
		substrings = set(map(str.lower,substrings))
	counts = dict.fromkeys(substrings,0)
	for i in substrings:
		if i in string:
			counts[i] += 1
	return counts
