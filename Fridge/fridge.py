magnets = input()
mag_map = {}

nums = "1234567890"

for x in nums:
    mag_map[x] = 0

for x in magnets:
    mag_map[x] += 1

smallestOccurence = 1001
key = None 

for num in nums:
    if mag_map[num] < smallestOccurence:
        key = num
        smallestOccurence = mag_map[num]

foundIt = False
for num in nums[:len(nums) - 1]:
    if mag_map[num] == 0:
        print(num)
        foundIt = True
        break

if not foundIt:
    if key == '0':
        print("1" + "0" * (smallestOccurence + 1 if mag_map['1'] > 0 else 0))
    else:
        print(key * (smallestOccurence + 1))
