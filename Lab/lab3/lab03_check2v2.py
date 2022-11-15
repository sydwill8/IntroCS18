


def calc_skew(t1,t2,t3,t4,t5):
    average = (t1 + t2 + t3 + t4 + t5)/5
    var = (t1 - average)**2 + (t2 - average)**2 + (t3 - average)**2 + (t4 - average)**2 + (t5 - average)**2
    var /= 5
    skew = (t1 - average)**3 + (t2 - average)**3 + (t3 - average)**3 + (t4 - average)**3 + (t5 - average)**3
    skew /= 5
    skew = skew/var**3**0.5
    return skew

def stats(n1,t1,t2,t3,t4,t5):
    minimum = min(t1, t2, t3, t4, t5)
    maximum = max(t1, t2, t3, t4, t5)
    average = ((t1 + t2 + t3 + t4 + t5) - minimum - maximum) / 3
    print("{0}'s stats --".format(n1), "min: {0:.0f}, max: {1:.0f}, avg: {2:.1f}".format(minimum, maximum, average))
    
    


name_1 = "Stan"
## The following are Stan's 5 latest running times for 3 miles

time1_1 = 34
time2_1 = 34
time3_1 = 35
time4_1 = 31
time5_1 = 29

name_2 = "Kyle"
## The following are Kyle's 5 latest running times for 3 miles

time1_2 = 30
time2_2 = 31
time3_2 = 29
time4_2 = 29
time5_2 = 28

name_3 = "Cartman"
## The following are Cartman's 5 latest running times for 3 miles
time1_3 = 36
time2_3 = 31
time3_3 = 32
time4_3 = 33
time5_3 = 33

name_4 = "Kenny"
## The following are Kenny's 5 latest running times for 3 miles
time1_4 = 33
time2_4 = 32
time3_4 = 34
time4_4 = 31
time5_4 = 35

name_5 = "Bebe"
## The following are Bebe's 5 latest running times for 3 miles
time1_5 = 27
time2_5 = 29
time3_5 = 29
time4_5 = 28
time5_5 = 30

# Process results for the first person

st = stats(name_1, time1_1, time2_1, time3_1, time4_1, time5_1)

kyl = stats(name_2, time1_2, time2_2, time3_2, time4_2, time5_2)

ca = stats(name_3, time1_3, time2_3, time3_3, time4_3, time5_3)

ken = stats(name_4, time1_4, time2_4, time3_4, time4_4, time5_4)

be = stats(name_5, time1_5, time2_5, time3_5, time4_5, time5_5)

'''
s = calc_skew(time1_1, time2_1, time3_1, time4_1, time5_1) 
print ("{0}'s running times have a skew of {1:.2f}".format(name_1, s))


## Process for the second person

ky = calc_skew(time1_2, time2_2, time3_2, time4_2, time5_2)
print ("{0}'s running times have a skew of {1:.2f}".format(name_2, ky))

## Process for the third person

c = calc_skew(time1_3, time2_3, time3_3, time4_3, time5_3)
print ("{0}'s running times have a skew of {1:.2f}".format(name_3, c))


## Process for the fourth person

ke = calc_skew(time1_4, time2_4, time3_4, time4_4, time5_4)
print ("{0}'s running times have a skew of {1:.2f}".format(name_4, ke))


## Process for the fifth person

b = calc_skew(time1_5, time2_5, time3_5, time4_5, time5_5)
print ("{0}'s running times have a skew of {1:.2f}".format(name_5, b)) '''
