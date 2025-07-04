def connectingTowns(n, routes):
    # Write your code here (np=no.of.paths)
    np=1
    for i in routes:
        np*=i
    return np%1234567



#without loops
def connectingTowns(n, routes):
    np=math.prod(routes)
    return np%1234567