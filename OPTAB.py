class OPTAB(object):
    def __init__(self):
        self.optab = {"MOV":"D2","ADD":"88"}
        
    def lookup(self,opcode):
    	if(opcode in self.optab.keys()):
    		return True
    def retrieve(self,opcode):
    	if(self.lookup(opcode)):
    		return self.optab[opcode]    
        

test = OPTAB()
test.lookup('ADD')
