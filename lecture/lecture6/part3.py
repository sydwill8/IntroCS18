''' Asks user for numbers'''

first = float(input("Enter the first number: "))
print(first)
second = float(input("Enter the second number: "))
print(second)

''' Determines if the user has entered two numbers that are both above or below the number 10'''
if ((first <= 10) and (second < 10)):
    print("Both are below 10.")

elif ((first >= 10) and (second > 10)):
    print("Both are above 10.")

''' Prints the average betweeen the two numbers the user entered'''
print("Average is",(round(((first + second) / 2), 2)))