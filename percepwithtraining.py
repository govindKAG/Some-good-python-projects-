#govindKAG 
inputs  = [[-1,-1,-1],[-1,1,1],[1,-1,1],[1,1,1]] #x1,x2,y

activate = lambda x:x > 0
f = lambda x:x == 1

def net(inputs, weights, bias):
    l =[i * j for i, j in zip(inputs, weights)]
    net = 0
    for i in l:
        net = net + i
    return net + bias

#hebb rule
def train(inputs):
 #   dw1 ,dw2,db = 0,0,0
    rw = [0,0,0]  # weights and bias is initialized to 0
    for i, j, k in inputs:
        rw[0] = i * k + rw[0]
        rw[1] = j * k + rw[1]
        rw[2] = k + rw[2]
        print(i * k, j * k, k, "      ", rw)
    return [rw[:2], rw[2]]

def evaluate(inputs, weights, bias):
    return activate(net(inputs, weights, bias))


print("input truth table \n ","-" * 2, "\n")
for j in inputs: print(j[:2],"---->", f(j[2]))
print("\n\nstarting to train \n","-" * 30, "\n")    
weights, bias = train(inputs)

print("\n\ntraining complete \n","-" * 30,"\n ")

print("weights and biases after training \n\tw1 = ",weights[0],\
      "\n\tw2 = ", weights[1],"\n\tbias = ", bias,\
      "\n\n Now testing exhaustively \n","-" * 30,"\n")

print("input","   ----> ","prediction")

for i in inputs:   
    #print(i,"   ----> ",activate(net(i[:2] , weights,bias)))
    print(i[:2], "   ----> ",evaluate(i[:2], weights,bias))


