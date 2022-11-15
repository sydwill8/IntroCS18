'''Program finds the percent average of the popultion of New York from 1790 to 2010'''

'''Author: Sydnee Williams'''

census = [ 340, 589, 959, 1372, 1918, 2428, 3097, 3880, 4382, 5082, \
            5997, 7268, 9113, 10385, 12588, 13479, 14830, 16782, \
            8236, 17558, 17990, 18976, 19378 ]

percents = []

i = 0
while i < (len(census) - 1):
    percents.append(((census[i + 1] - census[i]) / census[i]) * 100)
    i += 1
print("Average = {0:.1f}%".format(sum(percents) / len(percents)))