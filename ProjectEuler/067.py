import sys

# based on the exact same algo as 018.py

triangle = []

for line in sys.stdin:
    l = [int(x) for x in line.split()]
    triangle.append(l)

for i in range(1, len(triangle)):
    for j in range(len(triangle[i])):
        left = 0
        right = 0
        if j - 1 >= 0:
            left = triangle[i-1][j-1]
        if j < len(triangle[i-1]):
            right = triangle[i-1][j]
        triangle[i][j] += max(left, right)

print(max(triangle[-1]))