lastWord = input().strip()

words = []

for _ in range(int(input())):
    words.append(input().strip())

goodWords = [x for x in words if x[0] == lastWord[-1]]

for word in goodWords:
    if word != lastWord:
        eliminationWord = True 
        for snd in words:
            if snd != lastWord and snd != word:
                if word[-1] == snd[0]:
                    eliminationWord = False 
                    break
        if eliminationWord:
            print(word + "!")
            exit()

print(goodWords[0] if len(goodWords) > 0 else '?')