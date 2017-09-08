# class percptron:
# def __init__(self)

# or gate
inputs, weights, bias = [[-1, -1], [-1, 1], [1, -1], [1, 1]], [2, 2], 2


def activate(x): return x > 0


def net(inputs, weights, bias):
    l = [i * j for i, j in zip(inputs, weights)]
    net = 0
    for i in l:
        net = net + i
    return net + bias


for i in inputs:
    print(i, "   ----> ", activate(net(i, weights, bias)))
