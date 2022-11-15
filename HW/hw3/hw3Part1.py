'''Program will find the stastics of a name '''

'''Author: Sydnee Williams'''

import read_names

'''Reads the names from the text file'''
read_names.read_from_file("top_names_1880_to_2014.txt")

def total_female_names(years):
    (females,females_counts) = read_names.top_in_year(years, 'f')
    j = 0
    count = 0
    while j <= 249:
        count += females_counts[j]
        j += 1
    return count


def total_male_names(years):
    (males,males_counts) = read_names.top_in_year(years, 'M')
    j = 0
    count = 0
    while j <= 249:
        count += males_counts[j]
        j += 1
    return count


'''Finds the index of the name within the male and female lists'''
def index_of_female(years,names):
    (females,female_counts) = read_names.top_in_year(years, 'f')
    i  = 0
    count = 0
    while i <= 249:
        if females[i] == names:
            return count
        i += 1
        count += 1    

def index_of_male(years,names):
    (males,male_counts) = read_names.top_in_year(years, 'M')
    i  = 0
    count = 0    
    while i <= 249:
        if males[i] == names:
            return count
        else:
            return -1        
        i += 1
        count += 1
          

'''Asks user for input of a specific year and rank'''
year = int(input("Enter a year (1881-2013) => "))
print(year)

rank = int(input("Enter a rank (1-250) => "))
print(rank)





'''Accesses the names and count in the list'''
(female_names,female_counts) = read_names.top_in_year(year, 'f') 
(male_names,male_counts) = read_names.top_in_year(year, 'M') 



'''Making sure the rank and year are withn the appropriate ranges'''
if ((year > 2013) or (year < 1881)) or ((rank < 1) or (rank > 250)):
    print(year, "is not in the range 1881-2013 or", rank, "is not in the range 1-250")
    

'''Prints the statistics of a certain female name within a year'''
if ((year >= 1881) and (year <= 2013) and (rank >= 1) and (rank <= 250)):
    new_rank = rank - 1
    new_year = year
    number_female0 = total_female_names(new_year - 1)
    number_female = total_female_names(new_year)
    number_female2 = total_female_names(new_year + 1)
    
    number_male0 = total_male_names(new_year - 1)
    number_male = total_male_names(new_year)
    number_male2 = total_male_names(new_year + 1)
    
    new_name = female_names[new_rank]
    
     
    
    print("The rank", rank, "most popular female name in {:d} is {:s}\n\t".format(year, female_names[new_rank]) + "{0:.0f} out of {1:.0f} or {2:.2f}%".format(female_counts[new_rank], number_female, ((female_counts[new_rank] / number_female) * 100)   ))
    
    '''Prints the Histogram of a female name during a period of three years'''
    
    print("Histogram for {:s}". format(female_names[new_rank]))

    print("{0:.0f}:".format(year - 1) + ((int(((female_counts[index_of_female(year - 1, female_names[new_rank])] / number_female0) * 1000))) * "*") + "\t\t({0:.2f}%)".format(((female_counts[index_of_female(year - 1, female_names[new_rank])] / number_female0) * 100)))

    print("{0:.0f}:".format(year) + ((int(((female_counts[new_rank] / number_female) * 1000))) * "*") + "\t\t({0:.2f}%)".format(((female_counts[new_rank] / number_female) * 100)))

    print("{0:.0f}:".format(year + 1) + ((int(((female_counts[index_of_female(year + 1, female_names[new_rank])] / number_female2) * 1000))) * "*") + "\t\t({0:.2f}%)".format(((female_counts[index_of_female(year + 1, female_names[new_rank])] / number_female2) * 100)))
    


    '''Prints the statistics of a certain male name within a year'''
    print("The rank", rank, "most popular male name in {:d} is {:s}\n\t".format(year, male_names[new_rank]) + "{0:.0f} out of {1:.0f} or {2:.2f}%".format(male_counts[new_rank], number_male, ((male_counts[new_rank] / number_male) * 100)   ))

    '''Prints the Histogram of a male name during a period of three years'''
    print("Histogram for {:s}". format(male_names[new_rank]))

    print("{0:.0f}:".format(year - 1) + ((int(((male_counts[index_of_male(year - 1, male_names[new_rank])] / number_male0) * 1000))) * "*") + "\t\t({0:.2f}%)".format((int(male_counts[index_of_male(year - 1, male_names[new_rank])] / number_male0) * 100)))

    print("{0:.0f}:".format(year) + ((int(((male_counts[new_rank] / number_male) * 1000))) * "*") + "\t\t({0:.2f}%)".format(((male_counts[new_rank] / number_male) * 100)))

    print("{0:.0f}:".format(year + 1) + ((int(((male_counts[index_of_male(year + 1, male_names[new_rank])] / number_male0) * 1000))) * "*") + "\t\t({0:.2f}%)".format(((male_counts[index_of_male(year + 1, male_names[new_rank])] / number_male2) * 100)))
         
