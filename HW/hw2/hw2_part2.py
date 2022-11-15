''' This program will find the year it will be

Author: Sydnee Williams
'''

def time_to_seconds(hours, minutes, seconds):
    
    '''Turns hours, minutes, and seconds into seconds and returns seconds'''
    
    seconds = (hours * 3600) + (minutes * 60) + seconds
    return seconds

def calculate_years(total_d, total_c, change_in_number):
    convert_to_years_c = total_c // change_in_number
    convert_to_years_d = total_d // change_in_number
    return convert_to_years_d - convert_to_years_c


current_length = 86164
print("The current length of a day is", current_length, "seconds.")

desired_day = int(input("Enter the desired day length in seconds => "))
print(desired_day)
'''Turns the seconds into hours, minutes, and seconds'''

rate = (6 / 900000000) * 3600
year = 2018
hours = desired_day // 3600
minutes = (desired_day - (hours * 3600)) // 60
seconds = (desired_day - (hours * 3600)) % 60


print("\n{0:.0f} seconds is a day length of {1:.0f} hours {2:.0f} minutes and {3:.0f} seconds.".format(desired_day, hours, minutes, seconds))


print("A day change rate of", 6,"hours every", 900000000, "years,\nrepresents {0:.6f}".format(rate), "seconds per year.")

print("A day length of {0:.0f} hours, {1:.0f} minutes and {2:.0f} seconds,\nWould be in year {3:.0f}".format(hours, minutes, seconds, (calculate_years(desired_day, current_length, rate) + year)))
