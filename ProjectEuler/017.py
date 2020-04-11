underTwentyMap = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tensMap = ['padding', 'padding', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

#works up to 1000
def numToWord(n):
    if n < 20:
        return underTwentyMap[n]
    if n < 100:
        if n % 10 > 0:
            return tensMap[n // 10] + underTwentyMap[n % 10]
        else:
            return tensMap[n // 10]
    elif n < 1000:
        if n % 100 == 0:
            return underTwentyMap[n // 100] + 'hundred'
        else:
            return underTwentyMap[n // 100] + 'hundredand' + numToWord(n % 100)
    else:
        return 'onethousand'

ans = 0
for n in range(1, 1001):
    ans += len(numToWord(n))
print(ans)