score = int(input())

throws = []

while len(throws) <= 3:
    if score % 3 == 0:
        if score // 3 <= 20:
            throws.append("triple " + str(score // 3))
            break
        else:
            throws.append("triple 20")
            score -= 60
    elif score % 2 == 0:
        if score // 2 <= 20:
            throws.append("double " + str(score // 2))
            break
        else:
            throws.append("double 20")
            score -= 40
    else:
        if score <= 20:
            throws.append("single " + str(score))
            break 
        else:
            throws.append("single 20")
            score -= 20

if len(throws) <= 3:
    for throw in throws:
        print(throw)
else:
    print("impossible")