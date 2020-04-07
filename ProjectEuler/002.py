fibSequence = [1,2]
while fibSequence[-1] < 4000000:
    fibSequence.append(fibSequence[-1] + fibSequence[-2])

ans = 0
for val in fibSequence:
    if val % 2 == 0:
        ans += val
print(ans)