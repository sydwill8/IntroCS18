'''Program allows users to search locations by ZIP code, and determine the distances between the two locations'''

'''Author: Sydnee Williams'''


import hw4_util
import math


'''Returns a list of each elemtent within the dataset'''
zip_codes = hw4_util.read_zip_all()


'''Finds the ZIP code for a specific location'''
def zip_by_location(zip_codes, location):
    i = 0
    l = []
    location = (location[0].title(), location[1].upper())
    while i < len(zip_codes):
        if (location[0] in zip_codes[i][3]) and (location[1] in zip_codes[i][4]) :
            l.append(int(zip_codes[i][0]))
            i += 1
        else:
            i += 1
    
    return l


'''Finds the latitude, longitude, city, state, and county for a specific zip code'''
def location_by_zip(zip_codes, codes):
    i = 0
    codes = str(codes)
    while i < len(zip_codes):
        if codes in zip_codes[i][0]:
            return (zip_codes[i][1], zip_codes[i][2], zip_codes[i][3], zip_codes[i][4], zip_codes[i][5])
        
        else:
            i += 1
    
    return s



'''Checks to see if the zip code is within the list of zip codes'''
def check_zip(zip_codes, code):
    i = 0
    while i < len(zip_codes):
        if (code in zip_codes[i][0]):
            return True
        else:
            i += 1
    return False




'''User inputs a command'''
command = input("Command ('loc', 'zip', 'dist', 'end') => ")
print(command)
command = command.lower()






'''Ouputs the desired location, zip code, or distance'''
if command == 'loc':
    lookup_zip = (input("Enter a ZIP code to lookup => "))
    print(lookup_zip)
    
    if check_zip(zip_codes, lookup_zip) == False:
        print("Invalid or unknown ZIP code\n")
    else:
        
        degrees_la = int(location_by_zip(zip_codes, lookup_zip)[0])
        degrees_lo = int(location_by_zip(zip_codes, lookup_zip)[1])
        
        if degrees_la < 0:
            degrees_la = abs(degrees_la)
            minutes_la = abs(((location_by_zip(zip_codes, lookup_zip)[0]) % 1) * 60)
            seconds_la = abs((minutes_la % 1) * 60)
            if degrees_lo < 0:
                degrees_lo = abs(degrees_lo)
                minutes_lo = ((location_by_zip(zip_codes, lookup_zip)[1]) % 1) * 60
                seconds_lo = abs((minutes_lo % 1) * 60)                 
                print( "ZIP code", lookup_zip, "is in " + location_by_zip(zip_codes, lookup_zip)[2] + ", " + location_by_zip(zip_codes, lookup_zip)[3] + ", " + location_by_zip(zip_codes, lookup_zip)[4]+ " county,\n\tcoordinates: ({0:03d}\xb0{1:.0f}'{2:.2f}\"S,{3:03d}\xb0{4:.0f}'{5:.2f}\"W)\n".format(degrees_la, minutes_la, seconds_la, degrees_lo, minutes_lo, seconds_lo))
                
            elif degrees_lo > 0:
                minutes_lo = ((location_by_zip(zip_codes, lookup_zip)[1]) % 1) * 60
                seconds_lo = abs((minutes_lo % 1) * 60)                 
                print( "ZIP code", lookup_zip, "is in " + location_by_zip(zip_codes, lookup_zip)[2] + ", " + location_by_zip(zip_codes, lookup_zip)[3] + ", " + location_by_zip(zip_codes, lookup_zip)[4]+ " county,\n\tcoordinates: ({0:03d}\xb0{1:.0f}'{2:.2f}\"S,{3:03d}\xb0{4:.0f}'{5:.2f}\"E)\n".format(degrees_la, minutes_la, seconds_la, degrees_lo, minutes_lo, seconds_lo))
                
        elif degrees_la > 0:
            minutes_la = abs(((location_by_zip(zip_codes, lookup_zip)[0]) % 1) * 60)
            seconds_la = abs((minutes_la % 1) * 60)            
            if degrees_lo < 0:
                degrees_lo = abs(degrees_lo)
                minutes_lo = ((location_by_zip(zip_codes, lookup_zip)[1]) % 1) * 60
                seconds_lo = ((minutes_lo % 1) * 60)                 
                print( "ZIP code", lookup_zip, "is in " + location_by_zip(zip_codes, lookup_zip)[2] + ", " + location_by_zip(zip_codes, lookup_zip)[3] + ", " + location_by_zip(zip_codes, lookup_zip)[4]+ " county,\n\tcoordinates: ({0:03d}\xb0{1:.0f}'{2:.2f}\"N,{3:03d}\xb0{4:.0f}'{5:.2f}\"W)\n".format(degrees_la, minutes_la, seconds_la, degrees_lo, minutes_lo, seconds_lo))
                
            elif degrees_lo > 0:
                minutes_lo = ((location_by_zip(zip_codes, lookup_zip)[1]) % 1) * 60
                seconds_lo = abs((minutes_lo % 1) * 60)                 
                print( "ZIP code", lookup_zip, "is in " + location_by_zip(zip_codes, lookup_zip)[2] + ", " + location_by_zip(zip_codes, lookup_zip)[3] + ", " + location_by_zip(zip_codes, lookup_zip)[4]+ " county,\n\tcoordinates: ({0:03d}\xb0{1:.0f}'{2:.2f}\"N,{3:03d}\xb0{4:.0f}'{5:.2f}\"E)\n".format(degrees_la, minutes_la, seconds_la, degrees_lo, minutes_lo, seconds_lo))               
        
elif command == 'zip':
    city = input("Enter a city name to lookup => ")
    print(city)
    city = city.title()
    
    state = input("Enter the state name to lookup => ")
    print(state)
    state = state.upper()
    
    zip_by_location(zip_codes, (city,state))
    if zip_by_location(zip_codes, (city,state)) == []:
        print("No ZIP code found for", city + ', '+ state + '\n')
    else:
        new_tuple = tuple(zip_by_location(zip_codes, (city,state)))
        print("The following ZIP code(s) found for", city + ', ' + state + ':', str(new_tuple)[1: -1] + '\n')
        
        
elif command =='dist':
    zip1 = (input("Enter the first ZIP code => "))
    print(zip1)
    
    zip2 = (input("Enter the second ZIP code => "))
    print(zip2)
    
    if ((check_zip(zip_codes, zip1)) and (check_zip(zip_codes, zip2))) == True:
        zip1_la = float((location_by_zip(zip_codes, zip1)[0]) * 0.0174533)
        zip1_lo = float((location_by_zip(zip_codes, zip1)[1]) * 0.0174533)
        zip2_la = float((location_by_zip(zip_codes, zip2)[0]) * 0.0174533)
        zip2_lo = float((location_by_zip(zip_codes, zip2)[1]) * 0.0174533)
        
        change_latitude = zip2_la - zip1_la
        change_longitude = zip2_lo - zip1_lo
        
        a = ((math.sin((change_latitude / 2))) ** 2) + (math.cos(zip1_la) * math.cos(zip2_la) * ((math.sin((change_longitude / 2))) ** 2))
        
        distance = 2 * 3959.191 * math.asin(math.sqrt(a))
        
        print("The distance between", zip1, "and", zip2, "is {0:.2f} miles\n".format(distance))
    
   
    else:
        print("The distance between", zip1, "and", zip2, "cannot be determined\n")
else:
    if command != 'end':
        print("Invalid command, ignoring\n")



'''Repeats the following code until user enters END'''
while command != 'end':
    command = input("Command ('loc', 'zip', 'dist', 'end') => ")
    print(command)
    command = command.lower()
      
    
    if command == 'loc':
        lookup_zip = (input("Enter a ZIP code to lookup => "))
        print(lookup_zip)
        
        if check_zip(zip_codes, lookup_zip) == False:
            print("Invalid or unknown ZIP code\n")
        else:
            
            degrees_la = int(location_by_zip(zip_codes, lookup_zip)[0])
            degrees_lo = int(location_by_zip(zip_codes, lookup_zip)[1])
            
            if degrees_la < 0:
                degrees_la = abs(degrees_la)
                minutes_la = abs(((location_by_zip(zip_codes, lookup_zip)[0]) % 1) * 60)
                seconds_la = abs((minutes_la % 1) * 60)
                if degrees_lo < 0:
                    degrees_lo = abs(degrees_lo)
                    minutes_lo = ((location_by_zip(zip_codes, lookup_zip)[1]) % 1) * 60
                    seconds_lo = abs((minutes_lo % 1) * 60)                 
                    print( "ZIP code", lookup_zip, "is in " + location_by_zip(zip_codes, lookup_zip)[2] + ", " + location_by_zip(zip_codes, lookup_zip)[3] + ", " + location_by_zip(zip_codes, lookup_zip)[4]+ " county,\n\tcoordinates: ({0:03d}\xb0{1:.0f}'{2:.2f}\"S,{3:03d}\xb0{4:.0f}'{5:.2f}\"W)\n".format(degrees_la, minutes_la, seconds_la, degrees_lo, minutes_lo, seconds_lo))
                    
                elif degrees_lo > 0:
                    minutes_lo = ((location_by_zip(zip_codes, lookup_zip)[1]) % 1) * 60
                    seconds_lo = abs((minutes_lo % 1) * 60)                 
                    print( "ZIP code", lookup_zip, "is in " + location_by_zip(zip_codes, lookup_zip)[2] + ", " + location_by_zip(zip_codes, lookup_zip)[3] + ", " + location_by_zip(zip_codes, lookup_zip)[4]+ " county,\n\tcoordinates: ({0:03d}\xb0{1:.0f}'{2:.2f}\"S,{3:03d}\xb0{4:.0f}'{5:.2f}\"E)\n".format(degrees_la, minutes_la, seconds_la, degrees_lo, minutes_lo, seconds_lo))
                    
            elif degrees_la > 0:
                minutes_la = abs(((location_by_zip(zip_codes, lookup_zip)[0]) % 1) * 60)
                seconds_la = abs((minutes_la % 1) * 60)            
                if degrees_lo < 0:
                    degrees_lo = abs(degrees_lo)
                    minutes_lo = ((location_by_zip(zip_codes, lookup_zip)[1]) % 1) * 60
                    seconds_lo = ((minutes_lo % 1) * 60)                 
                    print( "ZIP code", lookup_zip, "is in " + location_by_zip(zip_codes, lookup_zip)[2] + ", " + location_by_zip(zip_codes, lookup_zip)[3] + ", " + location_by_zip(zip_codes, lookup_zip)[4]+ " county,\n\tcoordinates: ({0:03d}\xb0{1:.0f}'{2:.2f}\"N,{3:03d}\xb0{4:.0f}'{5:.2f}\"W)\n".format(degrees_la, minutes_la, seconds_la, degrees_lo, minutes_lo, seconds_lo))
                    
                elif degrees_lo > 0:
                    minutes_lo = ((location_by_zip(zip_codes, lookup_zip)[1]) % 1) * 60
                    seconds_lo = abs((minutes_lo % 1) * 60)                 
                    print( "ZIP code", lookup_zip, "is in " + location_by_zip(zip_codes, lookup_zip)[2] + ", " + location_by_zip(zip_codes, lookup_zip)[3] + ", " + location_by_zip(zip_codes, lookup_zip)[4]+ " county,\n\tcoordinates: ({0:03d}\xb0{1:.0f}'{2:.2f}\"N,{3:03d}\xb0{4:.0f}'{5:.2f}\"E)\n".format(degrees_la, minutes_la, seconds_la, degrees_lo, minutes_lo, seconds_lo))               
            
    elif command == 'zip':
        city = input("Enter a city name to lookup => ")
        print(city)
        city = city.title()
        
        state = input("Enter the state name to lookup => ")
        print(state)
        state = state.upper()
        
        zip_by_location(zip_codes, (city,state))
        if zip_by_location(zip_codes, (city,state)) == []:
            print("No ZIP code found for", city + ', '+ state + '\n')
        else:
            new_tuple = tuple(zip_by_location(zip_codes, (city,state)))
            print("The following ZIP code(s) found for", city + ', ' + state + ':', str(new_tuple)[1: -1] + '\n')
            
            
    elif command =='dist':
        zip1 = (input("Enter the first ZIP code => "))
        print(zip1)
        
        zip2 = (input("Enter the second ZIP code => "))
        print(zip2)
        
        if ((check_zip(zip_codes, zip1)) and (check_zip(zip_codes, zip2))) == True:
            zip1_la = float((location_by_zip(zip_codes, zip1)[0]) * 0.0174533)
            zip1_lo = float((location_by_zip(zip_codes, zip1)[1]) * 0.0174533)
            zip2_la = float((location_by_zip(zip_codes, zip2)[0]) * 0.0174533)
            zip2_lo = float((location_by_zip(zip_codes, zip2)[1]) * 0.0174533)
            
            change_latitude = zip2_la - zip1_la
            change_longitude = zip2_lo - zip1_lo
            
            a = ((math.sin((change_latitude / 2))) ** 2) + (math.cos(zip1_la) * math.cos(zip2_la) * ((math.sin((change_longitude / 2))) ** 2))
            
            distance = 2 * 3959.191 * math.asin(math.sqrt(a))
            
            print("The distance between", zip1, "and", zip2, "is {0:.2f} miles\n".format(distance))
        
       
        else:
            print("The distance between", zip1, "and", zip2, "cannot be determined\n")   
    
    else:
        if command != 'end':
            print("Invalid command, ignoring\n")
    
    

if command == 'end':
    print("\nDone")




'''print(location_by_zip(zip_codes, 12180))

print(zip_by_location(zip_codes, ('troy', 'nY')))

print(zip_codes[0])'''



