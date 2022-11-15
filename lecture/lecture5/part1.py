def convert2fahren(temp):
    
    ''' Create formula to convert from Celsius to Fahrenheit '''
    
    Fahrenheit = (temp * (9/5)) + 32
    return Fahrenheit

'''temp = 0'''
first = convert2fahren(0)
temp = 0
print(temp, "->", first)

second = convert2fahren(32)
temp = 32
print(temp, "->", second)

third = convert2fahren(100)
temp = 100
print(temp, "->", third) 