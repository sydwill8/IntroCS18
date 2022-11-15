'''Program is to list info for different restaurants'''

'''Author: Sydnee Williams'''


import lab05_util

def print_info(restaurant):
    l = []
    print(restaurant[0], '(' + restaurant[5] + ')\n\t' + restaurant[3].replace("+", "\n\t"))
    print("Average Score: {0:.2f}".format((sum(restaurant[6])) / len(restaurant[6])))
        



restaurants = lab05_util.read_yelp('yelp.txt')
print_info(restaurants[0])