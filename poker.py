from random import randrange

deck = ['A Hearts', '2 Hearts', '3 Hearts', '4 Hearts', '5 Hearts', '6 Hearts', '7 Hearts', '8 Hearts', '9 Hearts', '10 Hearts', 'J Hearts', 'Q Hearts', 'K Hearts', 'A Diamonds', '2 Diamonds', '3 Diamonds', '4 Diamonds', '5 Diamonds', '6 Diamonds', '7 Diamonds', '8 Diamonds', '9 Diamonds', '10 Diamonds', 'J Diamonds', 'Q Diamonds', 'K Diamonds', 'A Spades', '2 Spades', '3 Spades', '4 Spades', '5 Spades', '6 Spades', '7 Spades', '8 Spades', '9 Spades', '10 Spades', 'J Spades', 'Q Spades', 'K Spades', 'A Clubs', '2 Clubs', '3 Clubs', '4 Clubs', '5 Clubs', '6 Clubs', '7 Clubs', '8 Clubs', '9 Clubs', '10 Clubs', 'J Clubs', 'Q Clubs', 'K Clubs']

print('Welcome to ToC Texas Holdem')
royal_flush = False
count = 0
while not royal_flush:
    count = count + 1
    player1 = []
    player2 = []
    river = []
    while len(player1) < 2:
        card = randrange(len(deck))
        while deck[card] in player1 or deck[card] in player2:
            card = randrange(len(deck))
        player1.append(deck[card])
    while len(player2) < 2:
        card = randrange(len(deck))
        while deck[card] in player1 or deck[card] in player2:
            card = randrange(len(deck))
        player2.append(deck[card])
    while len(river) < 5:
        card = randrange(len(deck))
        while deck[card] in player1 or deck[card] in player2 or deck[card] in river:
            card = randrange(len(deck))
        river.append(deck[card])

    print('Player 1')
    print(player1)
    print('Computer')
    print(player2)
    print('River')
    print(river)
    if deck[0] in player1 or deck[0] in river:
        if deck[9] in player1 or deck[9] in river:
            if deck[10] in player1 or deck[10] in river:
                if deck[11] in player1 or deck[11] in river:
                    if deck[12] in player1 or deck[12] in river:
                        royal_flush = True
    if deck[0] in player2 or deck[0] in river:
        if deck[9] in player2 or deck[9] in river:
            if deck[10] in player2 or deck[10] in river:
                if deck[11] in player2 or deck[11] in river:
                    if deck[12] in player2 or deck[12] in river:
                        royal_flush = True
    if deck[13] in player1 or deck[13] in river:
        if deck[22] in player1 or deck[22] in river:
            if deck[23] in player1 or deck[23] in river:
                if deck[24] in player1 or deck[24] in river:
                    if deck[25] in player1 or deck[25] in river:
                        royal_flush = True
    if deck[13] in player2 or deck[13] in river:
        if deck[22] in player2 or deck[22] in river:
            if deck[23] in player2 or deck[23] in river:
                if deck[24] in player2 or deck[24] in river:
                    if deck[25] in player2 or deck[25] in river:
                        royal_flush = True
    if deck[26] in player1 or deck[26] in river:
        if deck[35] in player1 or deck[35] in river:
            if deck[36] in player1 or deck[36] in river:
                if deck[37] in player1 or deck[37] in river:
                    if deck[38] in player1 or deck[38] in river:
                        royal_flush = True
    if deck[26] in player2 or deck[26] in river:
        if deck[35] in player2 or deck[35] in river:
            if deck[36] in player2 or deck[36] in river:
                if deck[37] in player2 or deck[37] in river:
                    if deck[38] in player2 or deck[38] in river:
                        royal_flush = True
    if deck[39] in player1 or deck[39] in river:
        if deck[48] in player1 or deck[48] in river:
            if deck[49] in player1 or deck[49] in river:
                if deck[50] in player1 or deck[50] in river:
                    if deck[51] in player1 or deck[51] in river:
                        royal_flush = True
    if deck[39] in player2 or deck[39] in river:
        if deck[48] in player2 or deck[48] in river:
            if deck[49] in player2 or deck[49] in river:
                if deck[50] in player2 or deck[50] in river:
                    if deck[51] in player2 or deck[51] in river:
                        royal_flush = True

print('Found a Royal Flush in ' + str(count) + ' hands!!!')
