''' Program asks user for input and prints the difference, average, and median between the two numbers'''

'''Author: Sydnee Williams'''

values = [ 14, 10, 8, 19, 7, 13 ]

number1 = int(input("Enter a value: "))
print(number1)
number2 = int(input("Enter another value: "))
print(number2)


values.append(number1)
values.insert(2, number2)

print(values[3], values[-1])
print("Difference:", max(values) - min(values))
print("Average: {0:.1f}".format(sum(values) / len(values)))
values.sort()
print("Median: {0:.1f}".format(((values[len(values) // 2] + (values[(len(values) // 2) - 1])) / 2)))