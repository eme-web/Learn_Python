#Card Game. The program needs to represent a deck of 52 cards, which i'll build in a list.
#Each of the 52 elements in the list will be a dictionary(a set of key/value pairs). 
# To represent any card, each dictionary will contain three key/value pairs: 'rank','suit', 
# anad 'value'. the rank is the name of the card(Ace, 2,3,....10, Jack,Queen,King), 
# n=but the value ia an integer used for comparing cards(1,2,3,...10,11,12,13). 
# For example, the Jack of Clubs would be represented as the following dictionary:
#{'rank':'Jack','suit':'Clubs','value':11}. Before the player plays a round, the 
#list representing the deck is created and shuffled to randomize the order of the cards. 
#I have no graphical representation of the cards, so each time the user chooses
 #"Higher"or "lower", the program gets a card dictionary from the deck and prints the 
 #rank and suit for the user. The program then compares the value of the new card 
 #to that of the previous card and gives feedback based on the correctness of 
 #the user's answer.


#HigherorLower

import random
# Card constants
SUIT_TUPLE = ('Spades', 'Hearts','Clubs','Diamonds')
RANK_TUPLE = ('Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King')

NCARDS = 8

#Pass in a deck and this function returns a random card from the deck
def getCard(deckListIn):
    thisCard = deckListIn.pop() # pop i=one off the top of the deck and return
    return thisCard

    # Pass in a deck and this function returns a shuffled copy of the deck.
def shuffle(deckListIn):
    deckListOut = deckListIn.copy() # make a copy of thr starting deck
    random.shuffle(deckListOut)
    return deckListOut

# Main code
print('Welcome to Higher or Lower.')
print("You have to choose whether the next card to be shown will be higher or lower than the current card.")
print("Getting it right adds 20 points; get it wrong and you lose 15 points.")
print('You have 50 points to start.')
print()

startingDeckList = []
for suit in SUIT_TUPLE:
    for thisValue, rank in enumerate(RANK_TUPLE):
        cardDict = {'rank':rank, 'suit': suit, 'value':thisValue +1}
        startingDeckList.append(cardDict)

score = 50

while True: # play multiple games
    print()
    gameDeckList = shuffle(startingDeckList)
    currentCardDict = getCard(gameDeckList)
    currentCardRank = currentCardDict['rank']
    currentCardValue = currentCardDict['value']
    currentCardSuit = currentCardDict['suit']
    print('Starting card is: ', currentCardRank + ' of ' + currentCardSuit)
    print()

    for cardNumber in range(0,NCARDS): # play one game of this many cards
        answer = input('Will the next card be higher or lower than the' + currentCardRank + ' of ' + currentCardSuit + ' ? (enter h or l): ')
        answer = answer.casefold() # force lowercase
        nextCardDict = getCard(gameDeckList)
        nextCardRank = nextCardDict['rank']
        nextCardSuit = nextCardDict['suit']
        nextCardValue = nextCardDict['value']
        print('Next card is:', nextCardRank + ' of ' + nextCardSuit)

        if answer == 'h':
            if nextCardValue > currentCardValue:
                print('You got it right, it was higher')
                score = score + 20
            else:
                print('Sorry, it was not higher')
                score = score -15
        elif answer == 'l':
            if nextCardValue < currentCardValue:
                score = score + 20
                print("You got it right, it was lower")
            else:
                score = score - 15
                print('Sorry,it was not lower')
        print('Your score is:  ' score)
        print()
        currentCardRank = nextCardRank
        currentCardValue = nextCardValue

        goAgain = input('To play again, press ENTER, or "q" to quit: ')
        if goAgain == 'q':
            break

        print('Ok bye') 
                

