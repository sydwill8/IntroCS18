'''This program is used to determine if the user's sentence is happy, sad, or neutral.

Author: Sydnee Williams
'''

def number_happy(sentence):
        
        '''Finds the number of happy words within the string'''
        sentence = sentence.lower()
        count = 0
        
        if 'laugh' in sentence:
                count += 1
                sentence.replace('laugh', 'be')
                if 'laugh' in sentence:
                        count += 1
        if 'happiness' in sentence:
                count += 1
                sentence.replace('happiness', 'be')
                if sentence.find('happiness') == True:
                        count += 1                               
        if 'love' in sentence:
                count += 1
                sentence.replace('love', 'be')
                if sentence.find('love') == True:
                        count += 1                               
        if 'excellent' in sentence:
                sentence.replace('excellent', 'to')
                count += 1
                if sentence.find('excellent') == True:
                        count += 1                
        if 'good' in sentence:
                count += 1
                sentence.replace('good', 'be')
                if sentence.find('good') == True:
                        count += 1                                
        if 'smile' in sentence:
                count += 1
                sentence.replace('smile', 'be')
                if sentence.find('smile') == True:
                        count += 1                                
        return count



def number_sad(sentence):
        
        '''Finds the number of sad words within a string'''
        sentence = sentence.lower()
        count = 0
        if 'bad' in sentence:
                count += 1
                sentence.replace('bad', 'be')
                if sentence.find('bad') == True:
                        count += 1                
        if 'sad' in sentence:
                count += 1
                sentence.replace('sad', 'be')
                if sentence.find('sad') == True:
                        count += 1                                
        if 'terrible' in sentence:
                count += 1
                sentence.replace('terrible', 'be')
                if sentence.find('terrible') == True:
                        count += 1                               
        if 'horrible' in sentence:
                count += 1
                sentence.replace('horrible', 'be')
                if sentence.find('horrible') == True:
                        count += 1                               
        if 'problem' in sentence:
                count += 1
                sentence.replace('problem', 'be')
                if sentence.find('problem') == True:
                        count += 1                                
        if 'hate' in sentence:
                count += 1
                sentence.replace('hate', 'be')
                if sentence.find('hate') == True:
                        count += 1                              
        return count




sentence_orig =input("Enter a sentence => ")
sentence = sentence_orig.lower()


print(sentence_orig)


'''The following prints the sentiment and prints if the sentence is happy, sad, or neutral'''


if number_happy(sentence) > number_sad(sentence):
        
        print("Sentiment:", number_happy(sentence) * '+')
        print("This is a happy sentence.")
        
elif number_happy(sentence) == number_sad(sentence):
        
        print("Sentiment:", (number_happy(sentence) * "+" + number_sad(sentence) * "-")) 
        print("This is a neutral sentence.")
        
else:
        print("Sentiment:", number_sad(sentence) * '-')
        print("This is a sad sentence.")