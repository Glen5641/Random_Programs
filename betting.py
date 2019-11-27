from random import randrange
print('Welcome to ToC Roulette')
print('Min bet is 5 dollars')
numlosses = 0
numwins = 0
minbet = 1
bet = minbet
max = 0
ctr = 0
max_ctr = 0
val = int(input("How much do you want to start with: "))
while val > 0:
    ctr = ctr + 1
    odds = randrange(19)
    if(odds < 9):
        numwins = numwins + 1
        val = val + bet
        bet = minbet
        if max < val:
            max = val
            max_ctr = ctr
    else:
        numlosses = numlosses + 1
        val = val - bet
        bet = bet + bet

    print('you have ' + str(val) + ' dollars left.')
    print("Press enter to spin again.      Spin: " + str(ctr))
print('Highest Money: ' + str(max) + '     Max Spins: ' + str(max_ctr))
print('Losses: ' + str(numlosses) + '     Wins: ' + str(numwins))
