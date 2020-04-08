# Idea
# For each number get prime factorization, intersect all sets keeping track of counts, then take the product

upperRange = 20

def primeFactorization(num) -> [int]:
    p = 2
    ret = []
    while num > 1:
        if num % p == 0:
            ret.append(p)
            num = num // p
            p = 2
        elif p >= num:
            ret.append(p)
            break
        else:
            p += 1
    return ret 

#get all common prime factors
factors = {}
for i in range(1, upperRange + 1):
    #count the factors
    count = {}
    for x in primeFactorization(i):
        if x in count:
            count[x] += 1
        else:
            count[x] = 1
    # check if we have a new max
    for x in count:
        if x in factors and count[x] > factors[x] or x not in factors:
            factors[x] = count[x]


#take the product
prod = 1
for n in factors:
    prod *= n**factors[n]

print(prod)