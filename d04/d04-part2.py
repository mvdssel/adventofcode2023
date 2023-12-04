INPUT = 'd04/input-test.txt'
INPUT = 'd04/input.txt'

countPerCard = dict()
totalCardCount = 0

with open(INPUT) as f:
    for cardNr, card in enumerate(f):
        countPerCard[cardNr] = countPerCard.get(cardNr, 0) + 1

        cardTitle, cardNumbers = card.split(':')
        winningNumbers, myNumbers = cardNumbers.split('|')
        winningNumbers = set((int(n) for n in winningNumbers.split()))
        myNumbers = set((int(n) for n in myNumbers.split()))
        
        cardPoints = 0
        for myNumber in myNumbers:
            if myNumber in winningNumbers:
                cardPoints += 1
                countPerCard[cardNr + cardPoints] = (countPerCard.get(cardNr + cardPoints, 0) + countPerCard[cardNr])
        
        totalCardCount += countPerCard[cardNr]

print('There are {} cards.'.format(totalCardCount))