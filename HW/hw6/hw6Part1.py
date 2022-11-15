

'''Author: Sydnee Williams'''

def found(word_file, input_file):
    
    if (word_file in dict_set) == True:
        return True
    
    return False


def drop():
    
    
    
    return


def swap():
    
    
    
    
    return


def replace():
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    
    
    return





'''User input for name of the dictionary file and input file, and sets the words within the set'''

dict_set = set()
dictionary_file = input("Dictionary file => ")
print(dictionary_file)



for line in open(dictionary_file, encoding = 'ISO-8859-1'):
    word = line.strip()
    dict_set.add(word)
       

input_file = input("Input file => ")
print(input_file)


for index in open(input_file, encoding = 'ISO-8859-1'):
    word_file = index.strip()
    
    if found(word_file) == True:
        print(word_file + "{:15d}".format(word_file) + '->' + word_file + "{:15d}".format(word_file, end = '\n'))
    
    
    
        