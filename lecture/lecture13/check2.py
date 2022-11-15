
name_string1 = input("Enter the scores file: ")
name_string1 = name_string1.strip('\n')
print(name_string1)


name_string2 = input("Enter the output file: ")
name_string2 = name_string2.strip()
print(name_string2)
f_out = open(name_string2, 'w')


f = open(name_string1)
i = []

for line in f:
    i.append(int(line.strip('\n')))

i.sort()
k = 0
l = 0
for j in range(len(i)):
    if len(str(i[j])) == 2: 
        f_out.write("{0:.0f}:  {1:.0f}\n".format(l, i[j]))
        l += 1
        
    elif len(str(i[j])) == 1:
        f_out.write("{0:.0f}:   {1:.0f}\n".format(l, i[j]))
        l += 1
    elif len(str(i[j])) == 3:
        f_out.write("{0:.0f}: {1:.0f}\n".format(l, i[j]))
        l += 1  
        
f_out.close()
    