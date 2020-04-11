import re 

names = input().split("\",\"")
#get rid of the quotes on the last two names 
names[0] = names[0][1:]
names[-1] = names[-1][:len(names[-1]) - 1]

names.sort()

score = 0
for i in range(len(names)):
    score += sum(map(lambda x : ord(x) - ord('A') + 1, names[i])) * (i + 1)

print(score)