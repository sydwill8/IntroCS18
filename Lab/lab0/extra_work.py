def age():
    answer = raw_input("What is your age?")
    if answer <= 20 and answer >= 10:
        print "You are not worthy of being a donor"
    elif answer > 20 and answer <= 70:
        print "You are worthy of being a donor"
    else:
        print "You are not worthy"
        age()
        
age()