from collections import Counter
# sorry there are plenty things that you can reduce in here , but this works .


def formatter(resdict):
    """does the housekeeping and returns the required list"""
    l = list()
    for eachpower in sorted(resdict, reverse=True):
        if resdict[eachpower] != 0:
            l.append((resdict[eachpower], eachpower))
    return l
# def cleanup(l):
##    ret = []
# for i in l :
# ret.append(list(i))
# return ret


def dictify(p):
    d = dict()
    for i in p:
        if i[1] not in d.keys():
            d[i[1]] = i[0]
        else:
            d[i[1]] = d[i[1]] + i[0]
    return d


def add(d1, d2):
    c1, c2 = Counter(d1), Counter(d2)
    return dict(c1 + c2)


def multiply(l1, l2):
    res = []
    for i in l1:
        for j in l2:
            res.append((j[0] * i[0], j[1] + i[1]))
    return res
################ what matters #######################


def addpoly(p1, p2):
    if not p2:
        return p1
    elif not p1:
        return p2
    else:
        d1, d2 = dictify(p1), dictify(p2)
        res = add(d1, d2)
        result = formatter(res)
    return result


def multpoly(p1, p2):
    if not p2 or not p1:
        return []
    else:
        ##        l1,l2 = cleanup(p1), cleanup(p2)
        result = dictify(multiply(p1, p2))
        retval = formatter(result)
        return retval
