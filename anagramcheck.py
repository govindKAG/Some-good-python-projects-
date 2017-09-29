def anagramcheck(s1,s2):
	return sorted(s1,key = lambda x : ord(x.lower())) == sorted(s2,key = lambda x : ord(x.lower()))
