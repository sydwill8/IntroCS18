


def ok_to_add(row,column,number, bd):
    i = 0
    j = 0
    column = column - 1
    row = row - 1
    '''if (number or column or row) not in range(1,10):
        return False'''
    for i in range(len(bd)):
        if bd[row][i] == str(number):
            return False
        elif bd[i][column] == str(number):
            return False
        else:
            while i < 3:
                if (bd[row][i]) == str(number) or (bd[i][column]) == str(number):
                    return False
                else:
                    i += 1 
        

    
    return True

if __name__ == "__main__":
    bd = [ [ '1', '.', '.', '.', '2', '.', '.', '3', '7'],
           [ '.', '6', '.', '.', '.', '5', '1', '4', '.'],
           [ '.', '5', '.', '.', '.', '.', '.', '2', '9'],
           [ '.', '.', '.', '9', '.', '.', '4', '.', '.'],
           [ '.', '.', '4', '1', '.', '3', '7', '.', '.'],
           [ '.', '.', '1', '.', '.', '4', '.', '.', '.'],
           [ '4', '3', '.', '.', '.', '.', '.', '1', '.'],
           [ '.', '1', '7', '5', '.', '.', '.', '8', '.'],
           [ '2', '8', '.', '.', '4', '.', '.', '.', '6'] ]
    
    
    
    
    row = int(input("Enter a row (starting from 1) => "))
    column = int(input("Enter a column (starting from 1) => "))
    number = int(input("Enter a number => "))
    
    
    if ok_to_add(row, column, number, bd) == False:
        print("This number cannot be added")
    elif ok_to_add(row, column, number, bd) == True:
        bd[row - 1][column - 1] = number
        

def print_board(bd):
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
                
                
    return
                
    
