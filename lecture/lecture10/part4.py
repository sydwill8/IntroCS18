co2_levels = [ 320.03, 322.16, 328.07, 333.91, 341.47, \
               348.92, 357.29, 363.77, 371.51, 382.47, 392.95 ]

fraction = float(input("Enter the fraction: "))
print(fraction)

for number in range(len(co2_levels)):
    co2_levels[number] = co2_levels[number] * (1 + fraction)
    


print('First: {:.2f}'.format(co2_levels[0]))
print('Last: {:.2f}'.format(co2_levels[-1]))