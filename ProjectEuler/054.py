
# define some card ordering information
cardValue = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14
}

# first split up the hands for each player

player1Hands = []
player2Hands = []

for _ in range(1000):
    line = input()
    line = line.split()
    player1Hands.append([(c[0], c[1]) for c in line[:5]])
    player2Hands.append([(c[0], c[1]) for c in line[5:]])
    # sort the hands wrt card value
    player1Hands[-1].sort(key=lambda x: cardValue[x[0]])
    player2Hands[-1].sort(key=lambda x: cardValue[x[0]])

# define helper functions
# ALL FUNCTIONS ASSUME CARDS ARE SORTED BY CARD VALUE #
# ALL FUNCTIONS RETURN NONE TO SIGNIFY SUCH A HAND DOES NOT EXIST #
# YOU MAY ALSO ASSUME EVERY FUNCTION RETURNS THE VALUES IN ASCENDING ORDER #

def getCardValue(card):
    return cardValue[card[0]]


def getCardSuit(card):
    return card[1]


def getHighestCard(hand) -> int:
    """ return the index value of the highest card if one exists"""
    return getCardValue(hand[-1])


def getPair(hand) -> int:
    """ return the value of the highest pair if one exists"""
    for i in range(len(hand) - 1, 0, -1):
        if hand[i][0] == hand[i - 1][0]:
            return getCardValue(hand[i])
    return None


def getTwoPair(hand) -> (int, int):
    """ return the value of a two pair if one exists """
    if getCardValue(hand[0]) == getCardValue(hand[1]):
        if getCardValue(hand[3]) == getCardValue(hand[2]) or getCardValue(hand[3]) == getCardValue(hand[4]):
            return (getCardValue(hand[1]), getCardValue(hand[3]))
    elif getCardValue(hand[1]) == getCardValue(hand[2]):
        if getCardValue(hand[3]) == getCardValue(hand[4]):
            return (getCardValue(hand[1]), getCardValue(hand[3]))
    else:
        return None


def getThreeKind(hand) -> int:
    """ return the value of a three of a kind if one exists"""
    middle = getCardValue(hand[2])
    if middle == getCardValue(hand[3]) and middle == getCardValue(hand[4]):
        return middle
    elif middle == getCardValue(hand[0]) and middle == getCardValue(hand[1]):
        return middle
    else:
        return None


def getStraight(hand) -> int:
    """return the largest card in the straight if one exits"""
    start = getCardValue(hand[0])
    for i in range(1, len(hand)):
        if start == getCardValue(hand[i]) - 1:
            start = getCardValue(hand[i])
        else:
            return None
    return start


def hasFlush(hand) -> bool:
    """return true if a flush exists"""
    start = getCardSuit(hand[0])
    for i in range(1, len(hand)):
        if start != getCardSuit(hand[i]):
            return False
    return True


def getFullHouse(hand) -> (int, int):
    """return the two cards if a full house exists"""
    middle = getCardValue(hand[2])
    if middle == getCardValue(hand[0]) and middle == getCardValue(hand[1]):
        if getCardValue(hand[3]) == getCardValue(hand[4]):
            return (middle, getCardValue(hand[3]))
    elif middle == getCardValue(hand[3]) and middle == getCardValue(hand[4]):
        if getCardValue(hand[0]) == getCardValue(hand[1]):
            return (getCardValue(hand[0]), middle)
    else:
        return None

def fourOfAKind(hand) -> int:
    """return the value in the four of a kind if one exists"""
    if getCardValue(hand[1]) == getCardValue(hand[2]) and getCardValue(hand[2]) == getCardValue(hand[3]):
        if getCardValue(hand[2]) == getCardValue(hand[4]):
            return getCardValue(hand[2])
        if getCardValue(hand[2]) == getCardValue(hand[0]):
            return getCardValue(hand[2])
    return None

def straightFlush(hand) -> int:
    """return the largest value in a straight flush if one exists"""
    if hasFlush(hand):
        return getStraight(hand)
    else:
        return None


def royalFlush(hand) -> bool:
    """return true if a royal flush exists"""
    return hasFlush(hand) and getStraight(hand) == 14


def getHighestCardExcept(cards : [int], hand) -> int:
    """helper function, gets the highest card the is not one of the cards listed"""
    ans = 0
    for c in hand:
        if getCardValue(c) not in cards:
            ans = max(ans, getCardValue(c))

# compute the winners
player1Wins = 0
for i in range(1000):
    p1Hand = player1Hands[i]
    p2Hand = player2Hands[i]
    #royal flush
    if royalFlush(p1Hand) and not royalFlush(p2Hand):
        player1Wins += 1
        continue
    
    #straight flush
    if straightFlush(p1Hand) > straightFlush(p2Hand):
        player1Wins += 1
        continue

    #four of a kind
    if fourOfAKind(p1Hand) > fourOfAKind(p2Hand):
        player1Wins += 1
        continue
    elif fourOfAKind(p1Hand) == fourOfAKind(p2Hand):
        if getHighestCardExcept(fourOfAKind(p1Hand), p1Hand) > getHighestCardExcept(fourOfAKind(p2Hand), p2Hand):
            player1Wins += 1
        continue

    #get full house
    if getFullHouse(p1Hand) > getFullHouse(p2Hand):
        player1Wins += 1

    

