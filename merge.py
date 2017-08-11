def m(a,b):
    c = list()
    while len(a)!=0 and len(b)!=0:
        if a[0]<b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    if(len(a) == 0):
        return c+b
    if(len(b) == 0):
        return c+a

def ms(l):
    if(len(l)==0 or len(l) ==1):
        print("\tbase case returning ",l)
        return l
    else:
        print("merging ",l[:len(l)//2],"  and  ",l[len(l)//2:])
        return m(ms(l[:len(l)//2]), ms(l[len(l)//2:]))
    
        
        

