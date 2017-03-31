def orangecap(l):
    """ orangecape(dictionary of matches and players) -> (maxplayer,maxscore)
returns a tuple containing the name and score of the player who gets the orange cap"""
    highscores = {}
    for i in l.keys() : # i is a match 
        for j in l[i]: # j is a player rename them if you want 
                if j in highscores.keys()  :
                    highscores[j] = highscores[j]+l[i][j]
                elif j not in highscores.keys() : highscores[j] = l[i][j]
    maxplayer = max(highscores,key=highscores.get)
    return (maxplayer,highscores[maxplayer])

##NOTES    
## i have split it up into many steps so that it is easier to understand , you can squish this down a lot more                   
## i have also written it in python 2.7 , if it throws an error jus fix the incompatibility
## it shouldnt throw any errors as far as i can remember all this is compatible
                
## my sample case:
##d = {'m1':{'p1':450,'p2':200},'m2':{'p1': 300,'p3':100,'p2':800}}
##>>> player = orangecap(d)
##>>> player
##('p2', 800)
 