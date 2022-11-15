'''Program finds the minimum, maximum, and average of numbers inputed by user'''

'''Author: Sydnee Williams'''

numbers = []

i = 1
values = int(input("Enter a value (0 to end): "))
print(values)
while  values >= i :
        numbers.append(values)
        values = int(input("Enter a value (0 to end): "))
        print(values)
                
print("Min: {0:.0f}\nMax: {1:.0f}\nAvg: {2:.1f}".format(min(numbers), max(numbers), sum(numbers)/ len(numbers)))
