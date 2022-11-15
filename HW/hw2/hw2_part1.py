'''This program finds the amount of gumballs needed to fill a cube-sized gumball machine based-off of weekly sales.

Author: Sydnee Williams
'''

import math


def find_volume_sphere(radius):
    
    '''Returns the volume of a sphere'''
    
    volume = math.pi * radius ** 2
    return volume

def find_volume_cube(side):
    
    '''Returns volume of a cube'''
    
    volume = side ** 3
    return volume



radius = float(input('Enter the gum ball radius (in.) => '))
print(radius)

sales = int(input("Enter the weekly sales => "))
print(sales)

side_length = math.ceil((1.25 * sales) ** (1/3))


print("The machine needs to hold", side_length, "gum balls along each edge.")
print("Total edge length is {0:.2f} inches.".format((radius * 2) * side_length))
print("Target sales were {0:.0f}, but the machine will hold {1:.0f} extra gum balls.".format(math.ceil(sales * 1.25), find_volume_cube(side_length) - math.ceil(sales * 1.25)))
print("Wasted space is {0:.2f} cubic inches with the target number of gum balls,\nor {1:.2f} cubic inches if you fill up the machine.".format(((find_volume_cube(side_length) - (find_volume_sphere(radius)) * (math.ceil(sales * 1.25)))), ((find_volume_sphere(radius) * math.ceil(sales * 1.25) + (find_volume_cube(side_length) - math.ceil(sales * 1.25)))) / 2))