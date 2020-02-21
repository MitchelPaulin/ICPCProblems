testcases = int(input())

for t in range(testcases):
    input()
    vec1 = list(map(lambda x: int(x), input().split()))
    vec2 = list(map(lambda x: int(x), input().split()))
    vec1.sort()
    vec2.sort()

    dot_prod = 0
    for i in range(len(vec1)):
        dot_prod += vec1[i] * vec2[len(vec2) - i - 1]

    print("Case #%d: %d" % (t + 1, dot_prod))