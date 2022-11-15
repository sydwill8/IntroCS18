'''Program tells if the word is alternating or not based off of vowels and consonants'''

'''Author:Sydnee Williams'''

'''Determines if the word is alternating between vowels and consonants, and also f the alternating vowels are increasing'''
def is_alternating(word):
    value = True
    vowels = ['a', 'e', 'i', 'o', 'u']
    for x in (range(len(word) - 2)):
        if word[x] in vowels:
            if (word[x + 1] in vowels) == False:
                if ((word[x + 2]) < word[x]):
                    return False
            else:
                return True
                
    for i in (range(len(word) - 3)):      
        if word[i] not in vowels:
            if (word[i + 1] in vowels) == True:
                if ((word[i + 3]) < word[i + 1]):
                    return False
            else:
                return False
    return value
                    




words = input("Enter a word: ")
print(words)
word_low = words.lower()


'''Ouputs whether the word is alternating or not'''
if len(words) >= 8:
    if is_alternating(word_low) == True:
        print("The word", '\'' + words + '\'' , "is alternating\n")
    elif is_alternating(word_low) == False:
        print("The word", '\'' + words + '\'', "is not alternating\n")
    
else:
    if words != '':
        print("The word", '\'' + words + '\'' , "is not alternating\n")


while words != '':
    words = input("Enter a word: ")
    print(words)
    word_low = words.lower()
    
    
    if len(words) >= 8:
        if is_alternating(word_low) == True:
            print("The word", '\'' + words + '\'', "is alternating\n")
        elif is_alternating(word_low) == False:
            print("The word", '\'' + words + '\'', "is not alternating\n")
        
    else:
        if words != '':
            print("The word", '\'' + words + '\'', "is not alternating\n")

    