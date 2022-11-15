



import lab05_util

def print_info(restaurant):
    l = []
    print(restaurant[0], '(' + restaurant[5] + ')\n\t' + restaurant[3].replace("+", "\n\t"))
    
    if len(restaurant[6]) < 3:
        average = sum(restaurant[6]) / len(restaurant[6])

    else:
        average = ((sum(restaurant[6])) - max(restaurant[6]) - min(restaurant[6])) / len(restaurant[6])
    
    if (average >= 0) and (average < 2):
        print("This restaurant is rated bad, based on", len(restaurants[6]), "reviews")
    elif (average >= 2) and (average < 3):
        print("This restaurant is rated average, based on", len(restaurants[6]), "reviews")
    elif (average >= 3) and (average < 4):
        print("This restaurant is rated above average, based on", len(restaurants[6]), "reviews")
    elif (average >= 4) and (average <= 5):
        print("This restaurant is rated very good, based on", len(restaurants[6]), "reviews")
        



restaurants = lab05_util.read_yelp('yelp.txt')

number = int(input("Enter a number (start from 1): "))


if number > len(restaurants) or (number == 0):
    print("Value outside of range")
else:
    print_info(restaurants[number - 1])