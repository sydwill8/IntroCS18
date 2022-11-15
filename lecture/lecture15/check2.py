

imdb_file = input("Data file name: ").strip()
print(imdb_file)
prefix = input("Prefix: ").title()
print(prefix)

name_list = []
name3_set = set()
name_set = set(prefix)
names_set = set()
common = set()
counter = 0
count = 0
for line in open(imdb_file, encoding = "ISO-8859-1"):
    words = line.strip().split('|')
    name = words[0].strip()
    name_set.add(name)
    name3_set.add(name)




common = name_set.intersection(names_set)

print("{0:.0f} last names".format(len(name3_set)))
print("{0:.0f} start with". format(len(common)), prefix)


    


