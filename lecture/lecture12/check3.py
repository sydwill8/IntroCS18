

def find_min(l1):
    l2 = []
    i = 0
    while i < len(l1):
        l2.append(min(l1[i]))
        i += 1
    return min(l2)


if __name__ == "__main__":
    v = [ [ 11,12,3], [6, 8, 4], [ 17, 2, 18, 14] ]
    print("Min of list v: {}".format(find_min(v)) )
    u = [ [ 'car', 'tailor', 'ball' ], ['dress'], ['can', 'cheese', 'ring' ], \
              [ 'rain', 'snow', 'sun' ] ]
    print("Min of list u: {}".format(find_min(u)) )