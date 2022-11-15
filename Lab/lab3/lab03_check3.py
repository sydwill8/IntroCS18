''' This program is designed to find the population of foxes and bunnies in the \ 
following years

Author: Sydnee Williams
'''


def population_b(bpop,fpop):
    bpop_next = (10 * bpop) // (1 + 0.1 * bpop) - 0.05 * bpop * fpop
    return bpop_next

def population_f(bpop,fpop):
    fpop_next  = int(0.4 * fpop + 0.02 * fpop * bpop)
    return fpop_next


popb = int(input("Number of bunnies ==> "))
print(popb)
popf = int(input("Number of foxes ==> "))
print(popf)


print("Year 1: {0:.0f} {1:.0f}".format(popb,popf))

bpop_next = population_b(popb, popf)
fpop_next = population_f(popb, popf)

print("Year 2: {0:.0f} {1:.0f}".format(bpop_next, fpop_next))

bpop = bpop_next
fpop = fpop_next
bpop = population_b(bpop_next, fpop_next)
fpop = population_f(bpop_next, fpop_next)


print("Year 3: {0:.0f} {1:.0f}".format(bpop, fpop))

bpop_next = bpop
fpop_next = fpop
bpop_next = population_b(bpop, fpop)
fpop_next = population_f(bpop, fpop)

print("Year 4: {0:.0f} {1:.0f}".format(bpop_next, fpop_next))

bpop = bpop_next
fpop = fpop_next
bpop = population_b(bpop_next, fpop_next)
fpop = population_f(bpop_next, fpop_next)


print("Year 5: {0:.0f} {1:.0f}".format(bpop, fpop))