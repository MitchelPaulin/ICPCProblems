memo = [[0 for _ in range(21)] for _ in range(21)]

#set up base cases
for i in range(21):
    memo[0][i] = 1
    memo[i][0] = 1

#DP, T(i,j) = T(i-1,j) + T(i, j-1)
for i in range(1, 21):
    for j in range(1, 21):
        memo[i][j] = memo[i][j-1] + memo[i-1][j]

print(memo[20][20])