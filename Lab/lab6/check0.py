
'''i = 0
while i < 9:
    print(i, end = ' ')
    i += 1'''
    
'''print(*range(0,9))'''

'''for i in range(10):
    for j in range(10):
        
        print(i, end= ' ')'''
    
'''k = 1
l = 1
m = 1
for i in range(0,9):
    for j in range(0,9):
        if k == 3:
            if l == 9:
                if m == 27:
                    print((str(i) + ',' + str(j)), end = '\n\n')
                    k = 1
                    m = 1
                    l = 1
                else:
                    print((str(i) + ',' + str(j)), end = '\n')
                    k = 1
                    l = 1
                    m += 1
            else:
                print((str(i) + ',' + str(j)), end = '  ')
                l += 1
                k = 1
                m += 1
                
        else:
            print((str(i) + ',' + str(j)), end = ' ')
            k += 1
            l += 1
            m += 1
            
for j in range(0,9):
    print((str(2) + ',' + str(j)), end = ' ')

print('\n')
    
for i in range(0,9):
    print((str(i) + ',' + str(5)), end = ' ')

print('\n')'''
    
n = 1
for i in range(10):
    for j in range(10):
        if n == 10:
            print((str(i) + ',' + str(j)), end = '\n')
            n = 1
            
        else:
            print((str(i) + ',' + str(j)), end = ' ')
            n += 1
        