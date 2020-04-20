p = 1000

"""
This problem can be reduced to finding pythagorean triples
So what we can do is generate all pythagorean triples, sum them to get the perimeter and store the result in a map
Whichever result occurs most often at a certain p is the answer
"""

tripleList = set()

# Generate the triples, for this we can use Euclid's Formula
# Its required m > n > 0
def generatePythagoreanTiples(m, n):
    m2 = m * m
    n2 = n * n
    a = m2 - n2
    b = 2 * m * n 
    c = m2 + n2
    if a < b:
        return (a, b, c)
    return (b, a, c)

def perimeter(triple):
    return triple[0] + triple[1] + triple[2]

def mulTriple(triple, n):
    return (triple[0] * n, triple[1] * n, triple[2] * n)

for n in range(1, 100):
    for m in range(n + 1, 100):
        triple = generatePythagoreanTiples(m, n)
        perim = perimeter(triple) 
        if perim > p:
            break
        
        tripleList.add(triple)

        # get all integer multiples of the triple
        i = 2
        while True:
            newTrip = mulTriple(triple, i)
            perim = perimeter(newTrip)
            i += 1
            if perim < p:
                tripleList.add(newTrip)
            else:
                break

# roll up the triple list into a count 
d = {}
pAns = 0
maxCount = 0
for trip in tripleList:
    p = perimeter(trip)
    if p in d:
        d[p] += 1
    else:
        d[p] = 1
    if maxCount < d[p]:
        maxCount = d[p]
        pAns = p
print(pAns)