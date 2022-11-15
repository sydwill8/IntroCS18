

def parse_line(text):
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    i = 0
    j = 0
    count = 0
    l = [text]
    
    while i < len(text):
        texts = text.replace(',', '')
        texts = texts.replace('.', ' ')
        texts = texts.replace('\n', ' ')
        words3 = texts.split()
        words3 = words3[:-1]
        words3 = " ".join(words3)
        words = texts.split(" ")
        words2 = words[-1].replace("/", " ")         
        if text[i] == '/':
            count += 1
            i += 1
        elif (words2.isupper() == True) or (words2.islower() == True):
            return None        
        else:
            i += 1
    
               
    
    
    
    if count >= 3:
        j  = 0
        while j < len(text):
            if text[j] == "/":
                if text[j + 2] not in str(numbers):
                    j += 1
                    continue
                else:
                    words2 = []
                    if text[j + 1] in str(numbers):
                        texts = text.replace(',', '')
                        texts = texts.replace('.', ' ')
                        texts = texts.replace('\n', ' ')
                        words3 = texts.split()
                        words3 = words3[:-1]
                        words3 = " ".join(words3)
                        words = texts.split(" ")
                        words2 = words[-1].replace("/", " "). split()
                        
                        if '.' in text:
                            return(int(words2[0]), int(words2[1]), int(words2[2]), words3 + '.')
                        elif '\n' in text:
                            return(int(words2[0]), int(words2[1]), int(words2[2]), words3 + '\n')
                        else:
                            return(int(words2[0]), int(words2[1]), int(words2[2]), words3)
                    else:
                        return None
                    
            else:
                j += 1
                    
                                 
    
    return



print(parse_line("Here is some random text, like 5/4=3./12/3/4"))
print(parse_line("Here is some random text, like 5/4=3./12/3/4as"))
print(parse_line("Here is some random text, like 5/4=3./12/412/a/3/4"))
print(parse_line(" Here is some spaces 12/32/4"))
print(parse_line(" Again some spaces\n/12/12/12"))
