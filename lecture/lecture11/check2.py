'''Program outputs the height from tallest to shortest by using names'''

'''Author: Sydnee Williams'''

'''Appends heights to lists'''
l = []
hd = int(input("Enter Dale\'s height: "))
l.append(hd)
print(hd)

he = int(input("Enter Erin\'s height: "))
l.append(he)
print(he)

hs = int(input("Enter Sam\'s height: "))
l.append(hs)
print(hs)


'''Sorts out the list from tallest to shortest'''
if max(l) == hd:
    print("Dale")
    l.remove(hd)
    if max(l) == he:
        print("Erin")
        l.remove(he)
        print("Sam")
    else:
        if max(l) == hs:
            print("Sam")
            l.remove(hs)
            print("Erin")
        
            
elif max(l) == hs:
    print("Sam")
    l.remove(hs)
    if max(l) == he:
        print("Erin")
        l.remove(he)
        print("Dale")
    else:
        if max(l) == hd:
            print("Dale")
            l.remove(hd)
            print("Erin")

elif max(l) == he:
    print("Erin")
    l.remove(he)
    if max(l) == hd:
        print("Dale")
        l.remove(hd)
        print("Sam")
    else:
        if max(l) == hs:
            print("Sam")
            l.remove(hs)
            print("Dale")