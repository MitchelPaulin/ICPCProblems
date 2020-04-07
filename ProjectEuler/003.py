num = 600851475143
p = 2
largest = -1

while num > 1: 
    if num % p == 0:
        largest = max(largest, p)
        num = num // p
        p = 2
    elif p > num:
        largest = max(largest, num)
        break
    else:
        p += 1

print(largest)