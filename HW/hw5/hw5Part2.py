'''Program simulates a trainer moving in a direction and determining if the trainer encounters a pokemon, and if the trainer sees a pokemon, the trainer will throw a pokeball'''


'''Author: Sydnee Williams'''

import random

'''Function prints the dirction and a random value'''
def move_trainer():
    direction = ['N', 'E', 'S', 'W']
    
    return (random.choice(direction), float(random.random()))


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
    k = random.choice(values)
    return k


'''User Input'''
size = int(input("Enter the integer grid size => "))
print(size)

probability = float(input("Enter a probability (0.0 - 1.0) => "))
if probability == 1.0:
    probability = int(probability)
print(probability)

seed_value = (10 * size) + size
random.seed(seed_value)






location = [size // 2, size // 2]

i = 0
j = 1
turn = 0
pokemon = 0
capture = 0
missed = 0


while (location[0] != 0) and (location[1] != 0) and (location[0] != (size -1)) and (location[1] != (size - 1)):
    direction = move_trainer()
    
    if direction[0] == 'N':           
        turn += 1
        location[0] = location[0] - 1
        if direction[1] < probability:
            if i == 0:
                if throw_pokeball(3,j) == True:
                    print("Saw a pokemon at turn {0:.0f}, ".format(turn) + "location", tuple(location))
                    print("Caught it!") 
                    pokemon += 1
                    capture += 1
                    j += 1
                    i += 1
                else:
                    print("Saw a pokemon at turn {0:.0f}, ".format(turn) + "location", tuple(location))
                    print("Missed ...")
                    missed += 1
                    pokemon += 1
                
                
            else:
                if throw_pokeball(3, j) == True:
                    print("Saw a pokemon at turn {0:.0f}, ".format(turn) + "location", tuple(location))
                    print("Caught it!")
                    pokemon += 1
                    capture += 1
                    j += 1
                else:
                    print("Saw a pokemon at turn {0:.0f}, ".format(turn) + "location", tuple(location))
                    print("Missed ...")  
                    missed += 1
                    pokemon += 1

        
    elif direction[0] == 'S':
        turn += 1
        location[0] = location[0] + 1
        if direction[1] < probability:
            if i == 0:
                if throw_pokeball(3,j) == True:
                    print("Saw a pokemon at turn {0:.0f}, ".format(turn) + "location", tuple(location))
                    print("Caught it!") 
                    pokemon += 1
                    capture += 1
                    j += 1
                    i += 1
                else:
                    print("Saw a pokemon at turn {0:.0f}, ".format(turn) + "location", tuple(location))
                    print("Missed ...")
                    missed += 1
                    pokemon += 1
                
                
                
            else:
                if throw_pokeball(3, j) == True:
                    print("Saw a pokemon at turn {0:.0f}, ".format(turn) + "location", tuple(location))
                    print("Caught it!")
                    pokemon += 1
                    capture += 1
                    j += 1
                else:
                    print("Saw a pokemon at turn {0:.0f}, ".format(turn) + "location", tuple(location))
                    print("Missed ...")
                    missed += 1
                    pokemon += 1

        
    elif direction[0] == 'E':
        turn += 1
        location[1] = location[1] + 1
        if direction[1] < probability:
            if i == 0:
                if throw_pokeball(3,j) == True:
                    print("Saw a pokemon at turn {0:.0f}, ".format(turn) + "location", tuple(location))
                    print("Caught it!") 
                    pokemon += 1
                    capture += 1
                    j += 1
                    i += 1
                else:
                    print("Saw a pokemon at turn {0:.0f}, ".format(turn) + "location", tuple(location))
                    print("Missed ...")
                    missed += 1
                    pokemon += 1
                
                
            else:
                if throw_pokeball(3, j) == True:
                    print("Saw a pokemon at turn {0:.0f}, ".format(turn) + "location", tuple(location))
                    print("Caught it!")
                    pokemon += 1
                    capture += 1
                    j += 1
                else:
                    print("Saw a pokemon at turn {0:.0f}, ".format(turn) + "location", tuple(location))
                    print("Missed ...")
                    missed += 1
                    pokemon += 1

        
    elif direction[0] == 'W':
        turn += 1
        location[1] = location[1] - 1
        if direction[1] < probability:
            if i == 0:
                if throw_pokeball(3,j) == True:
                    print("Saw a pokemon at turn {0:.0f}, ".format(turn) + " location", tuple(location))
                    print("Caught it!") 
                    pokemon += 1
                    capture += 1
                    j += 1
                    i += 1
                else:
                    print("Saw a pokemon at turn {0:.0f}, ".format(turn) + " location", tuple(location))
                    print("Missed ...")
                    missed += 1
                    pokemon += 1
                
                
            else:
                if throw_pokeball(3, j) == True:
                    print("Saw a pokemon at turn {0:.0f},".format(turn) + " location", tuple(location))
                    print("Caught it!")
                    pokemon += 1
                    capture += 1
                    j += 1
                else:
                    print("Saw a pokemon at turn {0:.0f},".format(turn) + " location", tuple(location))
                    print("Missed ...")
                    missed += 1
                    pokemon += 1



if (location[0] == 0) or (location[1] == 0) or (location[0] == (size -1)) or (location[1] == (size - 1)):
    location = tuple(location)
    print("Trainer left the field at turn {0:.0f},".format(turn), "location ({0:.0f}, {1:.0f}).".format(location[0], location[1]))
    print(pokemon, "pokemon were seen,", capture, "of which were captured.")