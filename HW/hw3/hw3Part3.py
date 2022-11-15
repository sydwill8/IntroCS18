'''Program creates a game with Pikachu'''

'''Author: Sydnee Williams'''


'''Moves Pikachu'''
def move(x,y,direction):
    if direction == 'n':
        y -= 20
    if direction == 's':
        y += 20
    if direction == 'e':
        x += 20
    if direction == 'w':
        x -= 20
    if (x > 150) or (y > 150):
        if x > 150:
            x = 150
        else:
            y = 150
    if (x < 0) or (y < 0):
        if x < 0:
            x = 0
        else:
            y = 0
    return (x, y)


'''Prints Question'''

commands = []
energy = 10
i = 0
(p,z) = (75, 75)
while i <= 9:
    print("Pikachu at", (p,z), "with power", energy)
    question_1 = input("What does Pikachu do ('N', 'S', 'E', 'W', 'Attack', 'Rest')? ")
    commands.append(question_1)
    print(question_1)
       
    
    if (question_1.lower() == 'n') or (question_1.lower() == 's') or (question_1.lower() == 'e') or( question_1.lower() == 'w'):
        (p,z) = move((p,z)[0], (p,z)[1],question_1.lower())
        energy -= 1

        
    elif (question_1.lower() != 'n') or (question_1.lower() != 's') or (question_1.lower() != 'e') or (question_1.lower() != 'w') or (question_1.lower() != 'attack') or (question_1.lower() != 'rest'):
        energy -= 1
        if energy == 0:
            print("Pikachu is too tired!")
        
    if question_1.lower() == 'attack':
        if (energy < 5) and (energy > 0):
            energy -= 5
            print("Pffft, It's a dud ...")
            
        elif (energy < 0) or (energy == 0):
            energy == 0
            print("Pikachu is too tired!")
            
        elif energy >= 5:
            energy -= 4
            print("Bzzzt, Pikachu zaps its foe!")
            
    if question_1.lower() == 'rest':
        energy = 10
    
    if energy < 0:
        energy = 0
    i += 1
    

print("Pikachu at", (p,z), "with power", energy)
print("\nAll commands entered:")
print(commands)
print("All commands sorted:")
print(sorted(commands))