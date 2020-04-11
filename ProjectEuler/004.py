def isPalindrome(word):
    return word == word[::-1]

ans = 0
for n in range(1, 1000):
    for m in range(1, 1000):
        if n*m > ans and isPalindrome(str(n*m)):
            ans = n*m

print(ans)