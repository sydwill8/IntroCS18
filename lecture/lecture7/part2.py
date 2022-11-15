''' This program returns a single tupple.

Author: Sydnee Williams
'''

def add_tuples(x,y,z):
    add_x = x[0] + y[0] + z[0]
    add_y = x[1] + y[1] + z[1]
    new = (add_x, add_y)
    return new
    
    
    
    
print(add_tuples( (1,4), (8,3), (14,0) ))
print(add_tuples( (3,2), (11,1), (-2,6) ))