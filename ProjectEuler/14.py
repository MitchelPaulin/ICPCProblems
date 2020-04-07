lookup = {} # (start, sequence length)
lookup[1] = 1 # base case 

def collatz(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3*n + 1

def solve(x):
    if x in lookup:
        return lookup[x]
    else:
        y = solve(collatz(x)) + 1
        lookup[x] = y
        return y

count = 0
start = 0
for num in range(2, 1000001):
    lookup[num] = solve(num)
    if lookup[num] > count:
        count = lookup[num]
        start = num

print(start)