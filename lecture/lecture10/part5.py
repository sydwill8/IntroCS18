co2_levels = [ 320.03, 322.16, 328.07, 333.91, 341.47, \
               348.92, 357.29, 363.77, 371.51, 382.47, 392.95 ]

def is_increasing(values):
    for x in range(len(values)):
        if values[x] < values[x + 1]:
            return True
        elif values[x] > values[x + 1]:
            return False
    return


print('co2_levels is increasing: {}'.format(is_increasing(co2_levels)))
test_L1 = [ 15, 12, 19, 27, 45 ]
print('test_L1 is increasing: {}'.format(is_increasing(test_L1)))
test_L2 = [ 'arc', 'circle', 'diameter', 'radius', 'volume', 'area' ]
print('test_L2 is increasing: {}'.format(is_increasing(test_L2)))
test_L3 = [ 11, 21, 19, 27, 28, 23, 31, 45 ]
print('test_L3 is increasing: {}'.format(is_increasing(test_L3)))