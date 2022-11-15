def frame_string(word):
    return ('*' * len(word) + '*' * 6  + '\n') + ('*' * 2 + " " + word + " " + '*' * 2 + '\n') + ('*' * len(word) + '*' * 6) 
    
print((frame_string('Spanish Inquisition')) + '\n')

print(frame_string('Ni'))