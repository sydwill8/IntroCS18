import time

imdb_file = input("Enter the name of the IMDB file ==> ").strip()
counts = dict()
print(imdb_file)
count_list = []
start = time.time()
count = 0
for line in open(imdb_file, encoding = "ISO-8859-1"):
    words = line.strip().split('|')
    name = words[0].strip()
    #Walk through all the current entries loooking in
    #position [0] for the name we just found

    if name in counts:
        counts[name] += 1
    else:
        counts[name] = 1
        
maximum = max(sorted(counts.values()))
names = sorted(counts)
limit = min(100, len(names))
for index in range(limit):
    name = names[index]
    print("{} appeared in {} movies".format(name, counts[name])) 
    print("{} appear once".format(min(sorted(counts.values()))))

print("{} appears most often: {} times".format(sorted(list(counts.keys()))[0]),maximum)
