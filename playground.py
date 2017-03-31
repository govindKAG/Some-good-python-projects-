class tvShow(object):

	def __init__(self,title,season,episode,director="na",cast="na"):
		self.title = title 
		self.season = season 
		self.episode = episode
		#self.date = date 
		self.director = director
		self.cast = cast
		#self.currentEpisode = current
	def __str__(self):
		 return (self.title + "\n at season "+str(self.season) + "\n at episode" + str(self.episode))
		
		
class viewer(object):
	def __init__(self,name,shows):
		self.name = name 
		self.shows = shows
		self.currentlyWatching = len(self.shows)
	def listShows(self):
		print self.name,"\n"
		for s in self.shows:
			print s,"\n\n"
		

theSopranos = tvShow(title = "The sopranos",episode = 3, season = 3)
lost = tvShow(title = "lost",episode = 25, season = 6) 
fringe = tvShow(title = "fringe",episode = 10, season = 1) 
 
showlist = [theSopranos,lost,fringe]		
govind = viewer(name = "govind",shows= showlist )
govind.listShows()


