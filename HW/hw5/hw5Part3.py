'''Program repeats the simulation that was in Part 2 and outputs the statistics on the number of caughts and misses'''


'''Author: Sydnee Williams'''

import random
import math


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


def run_one_simulation(location, grid, probability):
    
    j = 1
    turn = 0
    pokemon = 0
    capture = 0
    missed = 0
    
    location = [size // 2, size // 2]
    
    while (location[0] != 0) and (location[1] != 0) and (location[0] != (size -1)) and (location[1] != (size - 1)):
        direction = move_trainer()
        
        if direction[0] == 'N':           
            turn += 1
            location[0] = location[0] - 1
            if direction[1] < probability:
                if throw_pokeball(3,j) == True:
                    count_grid[(location[0])][(location[1])] += 1
                    pokemon += 1
                    capture += 1
                    j += 1
                   
                else:
                    count_grid[(location[0])][(location[1])] -= 1
                    missed += 1
                    pokemon += 1
                    
    
            
        elif direction[0] == 'S':
            turn += 1
            location[0] = location[0] + 1
            if direction[1] < probability:
                if throw_pokeball(3,j) == True:
                    count_grid[(location[0])][(location[1])] += 1
                    pokemon += 1
                    capture += 1
                    j += 1
        
                else:
                    count_grid[(location[0])][(location[1])] -= 1
                    missed += 1
                    pokemon += 1
                    
    
            
        elif direction[0] == 'E':
            turn += 1
            location[1] = location[1] + 1
            if direction[1] < probability:
                if throw_pokeball(3,j) == True:
                    count_grid[(location[0])][(location[1])] += 1
                    pokemon += 1
                    capture += 1
                    j += 1
               
                else:
                    count_grid[(location[0])][(location[1])] -= 1
                    missed += 1
                    pokemon += 1
                    
    
            
        elif direction[0] == 'W':
            turn += 1
            location[1] = location[1] - 1
            if direction[1] < probability:
                if throw_pokeball(3,j) == True: 
                    count_grid[(location[0])][(location[1])] += 1
                    pokemon += 1
                    capture += 1
                    j += 1
    
                else:
                    count_grid[(location[0])][(location[1])] -= 1
                    missed += 1
                    pokemon += 1
                   
    
    
    
    return turn

def statistics():
    
    
    
    
    return



size = int(input("Enter the integer grid size => "))
print(size)

probability = float(input("Enter a probability (0.0 - 1.0) => "))
if (probability == 1.0) or (probability == 0.0):
    probability = int(probability)
print(probability)

simulations = int(input("Enter the number of simulations to run => "))
print(simulations)
print('')

seed_value = (10 * size) + size
random.seed(seed_value)



location = [size // 2, size // 2]



count_grid = []
for i in range(size):
    count_grid.append( [0]*size )
    
    

    
i = 0
turns =[]
grid = []
while i < (simulations):
    
    turns.append(run_one_simulation(location, size, probability))
    i += 1
    


n = 1
for i in range(len(count_grid)):
    for j in range(len(count_grid)):
        if n == size:
            print("{:5d}".format(count_grid[i][j]), end = '\n')
            n = 1
            
        else:
            print("{:5d}".format(count_grid[i][j]), end='')
            n += 1



k = 0
maximum_best = 0
while k < len(count_grid) - 1:
    if maximum_best < (max(count_grid[k])):
        maximum_best = max(count_grid[k])
        k += 1
    elif maximum_best == max(count_grid[k]):
        maximum_best = max(count_grid[k])
        k += 1
    else:
        k += 1
        
minimum_list = []       
for i in range(len(count_grid)):
    for j in range(len(count_grid)):
        minimum_list.append(count_grid[i][j])
        
        
minimum_best = min(minimum_list)

maximum = max(turns)
minimum = min(turns)
print(" Average number of turns in a simulation was {0:.2f}".format((sum(turns))/ simulations))
print("Maximum number of turns was {0:.0f} in simulation {1:.0f}".format(maximum,turns.index((maximum)) + 1))
print("Minimum number of turns was {0:.0f} in simulation {1:.0f}".format(minimum, turns.index((minimum)) + 1) )
print("Best net missed pokemon versus caught pokemon is {0:.0f}".format(maximum_best))
print("Worst net missed pokemon versus caught pokemon is {0:.0f}".format(minimum_best))