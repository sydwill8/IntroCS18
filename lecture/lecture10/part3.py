co2_levels = [ 320.03, 322.16, 328.07, 333.91, 341.47, \
               348.92, 357.29, 363.77, 371.51, 382.47, 392.95 ]

total = 0
values = 0
for number in co2_levels:
    total += number

average = total / len(co2_levels)
num_above = 0

for number in co2_levels:
    if number > average:
        num_above += 1
    

print("Average: {0:.2f}".format(average))
print("Num above average:", num_above)