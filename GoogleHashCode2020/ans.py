import heapq


class lib:
    books = None
    signup = None
    libId = None
    perDay = None
    visited = False

    def __init__(self, books, signup, libId, perDay):
        self.books = books
        self.signup = signup
        self.libId = libId
        self.perDay = perDay

    def __str__(self):
        return "{}: speed: {} singup: {} books: {}".format(self.libId,
                                                           self.perDay,
                                                           self.signup,
                                                           self.books)


books, libraries, days = map(lambda x: int(x), input().split(" "))

curDay = 0

scores = [int(x) for x in input().split(" ")]
w = sum(scores) / len(scores)

booksSeen = set()

libs = []

fScore = 0

for i in range(libraries):
    _, s, p = map(lambda x: int(x), input().split(" "))
    temp = []
    for x in input().split():
        t = int(x)
        temp.append((scores[t] * -1, t))
    libs.append(lib(temp, s, i, p))


libIds = []
booksSent = []

while curDay < days:
    bestLib = None
    bestScore = -99999999999
    seen = []

    # calculate best library
    for l in libs:
        if l.visited:
            continue

        daysLeft = days - curDay - l.signup
        obtainableBooks = daysLeft * l.perDay

        if obtainableBooks <= 0:
            continue

        score = 0
        temp = []

        # filter books
        libCopy = [b for b in l.books if b[1] not in booksSeen]
        l.books = libCopy[:]

        heapq.heapify(libCopy)

        while len(libCopy) > 0 and obtainableBooks > 0:
            book = heapq.heappop(libCopy)
            temp.append(book)
            obtainableBooks -= 1
            score += book[0] * -1

        score -= l.signup * w

        if score > bestScore:
            bestLib = l
            bestScore = score
            seen = temp

    if bestLib is None:
        break

    curDay += bestLib.signup
    bestLib.visited = True

    for b in seen:
        booksSeen.add(b[1])

    libIds.append(bestLib.libId)
    booksSent.append([b[1] for b in seen])

print(len(libIds))
for i in range(len(libIds)):
    print(libIds[i], len(booksSent[i]))
    for b in booksSent[i]:
        print(b, end=" ")
    print()
