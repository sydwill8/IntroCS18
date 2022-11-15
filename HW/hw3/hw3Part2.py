'''Program will find the correct change from a purchase'''

'''Author: Sydnee Williams'''

import hw3_util

file = input("Enter the coin file name => ")
print(file)

'''Opens and reads the file'''
coins = hw3_util.read_change(file)

cost_cents = int(input("Enter the item cost in cents (0-100) => "))
print(cost_cents)

print("I have the following coins:")
print(coins)

cents = 100 - cost_cents
print("Change from $1.00 is", cents, "cents")

coins.count(1)
coins.count(5)
coins.count(10)
coins.count(25)
coins.count(50)
    
if cents < 100:
    if coins.count(50) * 50 > cents:
        half_dollars = int(cents / 50)
        if (coins.count(25)) * 25 > cents:
            quarters = int(cents / 25)
            if (cents - (quarters * 25)) < 25:
                if coins.count(10) * 10 > cents:
                    dimes = int((cents - (quarters * 25))/10)
                    if (cents - int(((quarters * 25))/10)) < 10:
                        if (coins.count(5) * 5) > cents:
                            nickles = int(((cents - (quarters * 25))/10)/ 5)
                            if (cents - int((cents - (quarters * 25))/10)/ 5) < 5:
                                if (coins.count(1) * 1) > half_dollars:
                                    pennies = int((((cents - (quarters * 25))/10)/ 5))
