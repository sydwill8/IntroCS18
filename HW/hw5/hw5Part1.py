'''Program is the framework for the part 2 and part 3 of the homework. This program returns the 
grid size, and directions along with a random value'''


import random


'''Author: Sydnee Williams'''



'''Function prints the dirction and a random value'''
def move_trainer():
    direction = ['N', 'E', 'S', 'W']
    print("Directions:", direction)
    print("Selected", random.choice(direction) + ", value {0:.2f}".format(random.random()) )
    
    return


'''Function creates a list of True and False booleans and randomly prints one of the values within the list'''
def throw_pokeball(num_false, num_true):
    i = 0
    j = 0
    values = []
    while i < num_false:
        values.append(False)
        i += 1
        
    while j < num_true:
        values.append(True)
        j += 1
    
    
    print("Booleans:", values)
    print("Selected", random.choice(values))
    
    return


'''User input for size, value for False, and value for True, and then returns each one'''
size = int(input("Enter the integer grid size => "))
print(size)
num_false = int(input("Enter the integer number of Falses => "))
print(num_false)
num_true = int(input("Enter the integer number of Trues => "))
print(num_true)


'''Sets random.seed() to the grid multiplied by 11'''
grid = 11 * size
random.seed(grid)
print("Setting seed to", grid)


'''Calls the two functions throw_pokeball and move_trainer'''
i = 0
while i < 5:
    move_trainer()
    i += 1
    
j = 0
while j < 5:
    throw_pokeball(num_false, num_true)
    j += 1