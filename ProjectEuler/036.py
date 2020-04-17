"""
Make all palindromes by iterating over (up to) 3 digit numbers and appending them together
Also treat the case of single digit numbers as a special case
"""

def isBinPalindrome(x : int):
    s = bin(x)[2:]
    return s == s[::-1]


ans = 0

for i in range(1, 10):
    if isBinPalindrome(i):
        ans += i

for i in range(1, 1000):
    x = str(i)
    xr = x[::-1]
    pal = x + xr
    palN = int(pal)
    if isBinPalindrome(palN):
        ans += palN
    if(len(pal) < 6):
        for i in range(10):
            pal2N = int(x + str(i) + xr)
            if isBinPalindrome(pal2N):
                ans += pal2N
print(ans)