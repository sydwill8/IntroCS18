First_Name = input("Please enter your first name: ")
Last_Name = input("Please enter your last name: ")
Greeting = 'Hello,'
Longest = max(len(First_Name + "  "), len(Last_Name + "  "), len(Greeting + "  "))
print("*" * 2 + "*" * Longest  + "*" *2)
print("*" * 2, Greeting+" " * (Longest - len(Greeting + " ")) + "*" * 2)
print("*" * 2, First_Name + " " * (Longest - len(First_Name + " ")) + "*" * 2)
print("*" * 2, Last_Name + " " * (Longest - len(Last_Name + " ")) + "*" * 2)
print("*" * 2 + "*" * Longest  + "*" *2)