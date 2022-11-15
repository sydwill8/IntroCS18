'''Program finds the earlier semester and reports if it is True or False'''

'''Author: Sydnee Williams'''

def earlier_semester(x,y):
    if x[1] > y[1]:
        return False
    elif x[1] < y[1]:
        return True
    elif (x[0].lower() == y[0].lower()) and (x[1] == y[1]):
        return False
    else:
        if x[0].lower() == 'fall':
            return False
        else:
            return True
    return




when = ('Spring', 2015)

w1 = ('Spring',2015)
w2 = ('Spring',2014)
w3 = ('Fall', 2014)
w4 = ('Fall', 2015)
print( "{} earlier than {}? {}".format( w1, w2, earlier_semester(w1,w2)))
print( "{} earlier than {}? {}".format( w1, w1, earlier_semester(w1,w1)))
print( "{} earlier than {}? {}".format( w1, w4, earlier_semester(w1,w4)))
print( "{} earlier than {}? {}".format( w4, w1, earlier_semester(w4,w1)))
print( "{} earlier than {}? {}".format( w3, w4, earlier_semester(w3,w4)))
print( "{} earlier than {}? {}".format( w1, w3, earlier_semester(w3,w2)))








