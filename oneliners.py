def primeoneliner(lim):
        """ lim : int , upper bound non inclusive
            this function implements the sieve of erastothens method in oneline"""
        return [x for x in range(2,lim) if x not in [j for i in (2,3,5,7) for j in range (i*2,lim,i)]]






































def fact(num):
	if num <=1 :
		return 1

	return reduce(lambda a,b : a*b,range(1,num+1))
































