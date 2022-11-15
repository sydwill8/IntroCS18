import time


imdb_file = input("Enter the name of the IMDB file ==> ").strip()
count_list = []
start = time.time()
count = 0
for line in open(imdb_file, encoding = "ISO-8859-1"):
    count += 1
    if count % 1000 == 0:
        print(count)
    words = line.strip().split('|')
    name = words[0].strip()
    #Walk through all the current entries loooking in
    #position [0] for the name we just found
    
    found = False
    for pair in count_list:
        if name == pair[0]:
            pair[1] += 1
            found = True
            break
    if not found:
        count_list.append([name, 1])
        
        
end = time.time()
        