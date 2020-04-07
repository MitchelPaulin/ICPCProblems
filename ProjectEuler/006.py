def diffOfSquares(n):
    squareOfSum = ((n * (n + 1)) // 2)**2
    sumOfSquare = (n * (n + 1) * ((2 * n) + 1)) // 6
    return squareOfSum - sumOfSquare


print(diffOfSquares(100))
