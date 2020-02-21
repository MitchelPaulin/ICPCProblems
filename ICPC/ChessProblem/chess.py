n, m = input().split()

n = int(n)
m = int(m)

board = 1

while n != 0 and m != 0:
    chessboard = [[0 for _ in range(m)] for _ in range(n)]

    #list is 1 indexed, convert to 0     
    queenLine = list(map(lambda x: int(x) - 1, input().split()))
    knightLine = list(map(lambda x: int(x) - 1, input().split()))
    pawnLine = list(map(lambda x: int(x) - 1, input().split()))

    #add pawns 
    for i in range(1, len(pawnLine) - 1, 2):
        chessboard[pawnLine[i]][pawnLine[i+1]] = 2 

    # add knights and add attacked places 
    iModifier = [2, 2, -2, -2, 1, 1, -1, -1]
    jModifier = [1, -1, 1, -1 ,2, -2, 2, -2]
    for i in range(1, len(knightLine) - 1, 2):
        chessboard[knightLine[i]][knightLine[i + 1]] = 2
        for x in range(len(iModifier)):
            attackI = knightLine[i] + iModifier[x]
            attackJ = knightLine[i + 1] + jModifier[x]
            if attackI < 0 or attackI >= n:
                continue
            if attackJ < 0 or attackJ >= m:
                continue

            if chessboard[attackI][attackJ] != 2:
                chessboard[attackI][attackJ] = 1
    
    # add queens and add attack places
    qModI = [1,0,-1,0,1,-1,1,-1]
    qModJ = [0,1,0,-1,1,1,-1,-1]
    for i in range(1, len(queenLine) - 1, 2):
        chessboard[queenLine[i]][queenLine[i + 1]] = 2

        for j in range(len(qModI)):
            queenX = queenLine[i]
            queenY = queenLine[i + 1]
            while True: 
                queenX += qModI[j]
                queenY += qModJ[j]
                if queenX < 0 or queenX >= n:
                    break
                if queenY < 0 or queenY >= m:
                    break
                if chessboard[queenX][queenY] == 2:
                    break 
                
                chessboard[queenX][queenY] = 1


    #count zeros 
    ans = 0
    for row in chessboard:            
        ans += row.count(0)

    print("board " + str(board) + " has " + str(ans) + " spaces")

    board += 1

    n, m = input().split()

    n = int(n)
    m = int(m)
