bd = [ [ '1', '.', '.', '.', '2', '.', '.', '3', '7'],
       [ '.', '6', '.', '.', '.', '5', '1', '4', '.'],
       [ '.', '5', '.', '.', '.', '.', '.', '2', '9'],
       [ '.', '.', '.', '9', '.', '.', '4', '.', '.'],
       [ '.', '.', '4', '1', '.', '3', '7', '.', '.'],
       [ '.', '.', '1', '.', '.', '4', '.', '.', '.'],
       [ '4', '3', '.', '.', '.', '.', '.', '1', '.'],
       [ '.', '1', '7', '5', '.', '.', '.', '8', '.'],
       [ '2', '8', '.', '.', '4', '.', '.', '.', '6'] ]

print(len(bd))
print(len(bd[0]))
print(bd[0][0])
print(bd[8][8])

k = 1
l = 1
m = 1
o = 0
p = 27
print("-" * (len(bd) + 16))
for i in range(len(bd)):
    for j in range(len(bd)):
        if ((i == 0) or (i == 3) or (i == 6)) and (j == 0):
            print('| ', end = '')
            o += 1
        if k == 3:
            if l == 9:
                if m == 27:
                    print(str(bd[i][j]), end = ' |\n')
                    print(("-" * (len(bd) + 16)))
                    m = 1
                    l = 1
                    k = 1
                    p = 27
                else:
                    print(str(bd[i][j]), end = ' |\n| ')
                    l = 1
                    k = 1
                    m += 1
                    p -= 1
                
            else:
                print(str(bd[i][j]), end = ' | ')
                k = 1
                l += 1
                m += 1
                p -= 1
        else:
            print(str(bd[i][j]), end = ' ')
            k += 1
            l += 1
            m += 1
            p -= 1
            o += 1        
            
        