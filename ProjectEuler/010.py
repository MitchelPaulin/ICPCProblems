#use sieve of erastone
table = [True for _ in range(2000000)]
table[0] = False # for this question we do no count one as prime

for i in range(1, len(table)):
    if table[i]:
        step = (i + 1)
        num = step + step
        while num <= len(table):
            table[num - 1] = False
            num += step

ans = 0
for i in range(len(table)):
    if table[i]:
        ans += i + 1
print(ans)