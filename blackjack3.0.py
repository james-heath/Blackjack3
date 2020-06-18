
import random

def main(): # Title menu to start
    
    class Card(object): # Create an instance of a card object. The Deck class creates an instance of a card.
        def __init__(self, suit, rank):
            self.suit = suit
            self.rank = rank
            self.value = []
            
            if self.rank == "Ace": # This lot assigns a value attribute to each card instance
                self.value = 11
            elif self.rank == '2':
                self.value = 2
            elif self.rank == '3':
                self.value = 3
            elif self.rank == '4':
                self.value = 4
            elif self.rank == '5':
                self.value = 5
            elif self.rank == '6':
                self.value = 6
            elif self.rank == '7':
                self.value = 7
            elif self.rank == '8':
                self.value = 8
            elif self.rank == '9':
                self.value = 9
            else:
                self.value = 10
                   
        def show(self): # Shows a card instance as a readable string
            print('{} of {}'.format(self.rank, self.suit))

        def __repr__(self): # by defining this method the class can control what this function returns for its instances
            return '{} of {}'.format(self.rank, self.suit)
        
        def showValue(self): # Same as above but with the value 
            print('{} of {} has a value of {}'.format(self.rank, self.suit, self.value))
         
    #Testing of card instance
    #card = Card("Clubs", '5')
    #card.show()
    #card.value
    #card.showvalue()

    class Deck(object):
        def __init__(self):
            self.cards = []
            self.build()

        def build(self): # Creates a Deck and lists them in order so attribute self.cards.
            for s in ["Hearts", "Spades", "Diamonds", "Clubs"]:
                for r in ['2','3','4','5','6','7','8','9','10',
                         'Jack', 'Queen', 'King', 'Ace']:
                   self.cards.append(Card(s, r))
                    
    #    def build(self): # Creates a Deck as above just for testing purposes.
    #        for s in ["Hearts", "Spades", "Diamonds", "Clubs"]:
    #            for r in ['King']:
    #                self.cards.append(Card(s, r))                
                       
        def show(self): # Shows the list of cards in the Deck (self.cards list)
            for c in self.cards:
                c.show()
               
        def showValue(self):
            for c in self.cards:
                c.showValue()
                
        def shuffle(self): # Shuffles the deck
            for i in range(len(self.cards)-1, 0, -1): # In range -1 to start from the eend of the list; 0 to go to the begining and a step of 1.
                r = random.randint(0, i) # The 0 is the start i is the stop arguments .
                self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

        def newDeckCheck(self): # If length of deck is less than 75 cards it creates a new one
            if len(self.cards) < 75:
                deck = Deck()
                deck.sixPackDeck()
                deck.shuffle()
       
        def draw(self): # returns the popped last card from the Deck self.cards list.
            return self.cards.pop()
        
        def __len__(self): # Unnecessary bit to count the cards in the Deck (self.cards list)
            return len(self.cards)

        def sixPackDeck(self):
            self.cards = self.cards * 6

    
    deck = Deck() # Creates a deck of 52
    deck.sixPackDeck() # Makes a deck of six packs
    deck.shuffle()
    
    #Testing
    #deck.show() # shows the deck
    #deck.showValue() # Shows the deck and the card values
    #len(deck)
    #deck.draw()

    class Player(object):
        def __init__(self, name):
            self.name = name
            self.bank = 100
            self.hand = []
            self.handValue = []
            self.secHand = []
            self.secHandValue = []
            self.bet = []
            self.secBet = []
            self.sideBet = []
            self.bust = False
            self.secBust = False
            
        def draw(self, deck): # Draws a card from the deck instance in the Deck class (appends to player hand attribute list and pops from Deck cards list)
            self.hand.append(deck.draw())
            return self
           
        def drawSecHand(self, deck): # Same as above but adds to second hand attribute for when hand is split
            self.secHand.append(deck.draw())
            return self
        
        def hit(self): # 
            while True: # For main hand
                displayInfo()
                if self.handValue < 21:
                    ans = input("\nPress Enter to hit or 'n' to stand ").lower()
                    if ans == 'n':
                        break
                    else:
                        self.draw(deck)
                elif self.handValue > 20:
                    break   
            if self.secHand: # for secondhand
                while True:
                    displayInfo()
                    if self.secHandValue < 21:
                        ans = input("\n2nd hand - Press Enter to hit or 'n' to stand ").lower()
                        if ans == 'n':
                            break
                        else:
                            self.drawSecHand(deck)
                    elif self.secHandValue > 20:
                        break
                  
        def showHand(self): # Shows player hand/s values
                
            def calcValue(): # Works out the value of the players hand
                self.handValue = sum(c.value for c in self.hand)
                self.secHandValue = sum(c.value for c in self.secHand)

            def aceCheck():# looks for aces in player hand and makes it a 1 if hand is bust
                for c in self.hand: # Ace check for main hand
                    if c.value == 11:
                        if self.handValue > 21:
                            self.handValue = self.handValue - 10
                for c in self.secHand: # Ace check for second hand
                    if c.value == 11:
                        if self.secHandValue > 21:
                            self.secHandValue = self.secHandValue - 10
                          
            def showHand():
                h = []
                sh = []
                y = "\nYour hand    : "
                s = "\nYour 2nd hand: "
                if self.hand:
                    for c in self.hand:
                        h.append(str(c)) 
                    if self.handValue > 21:
                        self.bust = True
                        print(y, ", ".join(h), "for", self.handValue, " - Bust")
                    elif self.handValue == 21:
                        print(y, ", ".join(h), "for", self.handValue, " - Blackjack")
                    else:  
                        print(y, ", ".join(h), "for", self.handValue)               
                
                if self.secHand:
                    for c in self.secHand:
                        sh.append(str(c)) 
                    if self.secHandValue > 21:
                        self.secBust = True
                        print(s, ", ".join(sh), "for", self.secHandValue, " - Bust")
                    elif self.secHandValue == 21:
                        print(s,", ".join(sh), "for", self.secHandValue, " - Blackjack")
                    else:  
                        print(s, ", ".join(sh), "for", self.secHandValue)          
            
            calcValue()
            aceCheck()
            showHand()
        
        def showBank(self): # Shows the player name and the bank balance. Now inside the displayInfo() function
            print("Name:", self.name, "\nBank: $", self.bank)
       
        def showBet(self): # Shows the player bet/s now inside the displayInfo() function
            if self.bet:
                print("Bet: $", self.bet)
            if self.sideBet:
                print("Side bet: $", self.sideBet)
            if self.secBet:
                print("Second bet: $", self.secBet)
              
        def reset(self): # Resets the hand/s (clears info for start)
            self.hand = []
            self.handValue = []
            self.secHand = []
            self.secHandValue = []
            self.bust = False
            self.secBust = False
        
        def makeBet(self): # requests a int input adds to bet and deducts from bank 
            if self.bet == []:
                while True:
                    displayInfo()
                    try: # Stops crashing when non-int is input
                        x = float(input("\nPlace Bet: "))
                        if x in range(5,101) and x <= self.bank:
                            self.bet = x
                            self.bank -= x
                            break
                        elif x > self.bank:
                            input("Short of funds")
                        else:
                            input("Minimum bet $5, Maximum bet $100")
                    except ValueError:
                        input("That is not a number")
                           
        def makeSideBet(self):
            maxbet = self.bet / float(2)
            if self.bank >= 2.5:
                while True:
                    try: # Stops crashing when non-int is input
                        x = float(input("\nSide bet ammount (min $2.5, max ${}): ".format(maxbet))) 
                        if x >= 2.5 and x <= maxbet and x <= self.bank:
                            self.sideBet = x
                            self.bank -= x
                            break                
                        elif x > self.bank:
                            input("Short of funds")
                        else:
                            input("Minimum side bet $2.5, Maximum side bet ${} ".format(maxbet))
                    except ValueError:
                        input("That is not a number")
            else:
                input("Not enough for minimum bet")
                
        def doubleDown(self): # Checks if player can double down and asks
            if self.bank >= self.bet:
                if len(self.hand) == 2:
                    if self.handValue in range(9, 12):
                        while True:
                            displayInfo()
                            ans = input("\nDouble down? y/n ").lower()
                            if ans == 'y':
                                self.bank -= self.bet
                                self.bet += self.bet
                                self.draw(deck)
                                dealerPlay()
                                settlement()
                            elif ans == 'n':
                                break

        def splitPair(self): # Checks if can split pair and asks         
            x = []
            if self.bank >= self.bet:
                if len(self.hand) == 2:
                    for c in self.hand: 
                        x.append(c.rank)            
                    if x[0] == x[1]:  
                        while True:
                            displayInfo()
                            ans = input("\nSplit pair? y/n ").lower()
                            if ans == 'y':
                                self.secHand.append(self.hand.pop())
                                self.secBet = self.bet
                                self.bank -= self.bet
                                break
                            elif ans == 'n':
                                break
                               
            def acesCheck(self): # An ace check just for split pairs - deals a single card to each.
                if self.secHand:
                    x = []
                    for c in self.hand:
                        x.append(c.rank)
                    if x[0] == "Ace":
                        self.draw(deck)
                        self.drawSecHand(deck)
                        dealerPlay()
                        settlement()       
            
            acesCheck(self)
        
        def insurance(self): # 
            if len(dealer.hand) == 1:
                for c in dealer.hand:
                    if c.rank == "Ace":
                        while True:
                            displayInfo()
                            ans = input("\nDealer has an Ace, make an insurance side bet? y/n ").lower()
                            if ans == 'y':
                                self.makeSideBet()
                                break
                            elif ans == 'n':
                                break             

    #Testing
    #player = Player("Jim") # Creates a Player() class called "Jim"
    #player.bet = 50
    #player.draw(deck) # Draws a card instance from Deck list and and puts in hand of the player instance
    #player.hit() # Asks to hit only if handValue < 21.
    #player.showBank() # Prints the player instance name and bank prettily
    #player.showHand()# Prints the hand of the player and its value on one line.
    #player.makeBet() # Asks player to input a bet between 5 and 100. Subtracts from bank and adds to bet.
    #player.makeSideBet() 
    #player.doubleDown() # checks if first two cards = 9, 10, 11 and gives one more card and 
    #player.splitPair()
    #player.showBet()
    #len(deck)
    #displayInfo()

    class Dealer(object):
        def __init__(self):
            self.name = "Dealer"
            self.bank = 10000
            self.hand = []
            self.handValue = []
            self.bust = False
            
        def draw(self, deck): # Draws a card from the deck instance in the Deck class (appends to player hand attribute list and pops from Deck cards list)
            self.hand.append(deck.draw())
            return self
                 
        def showHand(self): # Shows player hand, hand value and whether but or blackjack on one line. 
                
            def calcValue(self): # Works out the value of the players hand
                self.handValue = sum(c.value for c in self.hand)
            
            def aceCheck():# looks for aces in dealer hand and makes it a 1 if hand is bust
                for c in self.hand:
                    if c.value == 11:
                        if self.handValue > 21:
                            self.handValue = self.handValue - 10

            def showHand(self):
                h = []
                d = "\nDealer's Hand: "
                for c in self.hand:
                    h.append(str(c)) 
                if self.handValue > 21:
                    self.bust = True
                    print(d, ", ".join(h), "for", self.handValue, " - Bust")
                elif self.handValue == 21:
                    print(d, ", ".join(h), "for", self.handValue, " - Blackjack")
                else:  
                    print(d, ", ".join(h), "for", self.handValue)

            if self.hand:
                calcValue(self)
                aceCheck()
                showHand(self)
                    
        def hit(self): # This draws a card only if handValue below 17
            while True:
                displayInfo()
                if self.handValue < 17:
                    self.draw(deck)
                else:
                    break

        def reset(self): # To return a card but no logic yet
            self.hand = []
            self.handValue = [] 
            self.bust = False
                      
    dealer = Dealer()
    
    #Testing
    #dealer.draw(deck)
    #dealer.showHand()
    #dealer.hit()   
    
    def gameHelp():
        print("""

Pg 1/3

You will attempt to beat the Dealer by getting a count as close to 21
as possible, without going over 21 (that is called going "Bust")

An Ace rank value is 1 or 11, face cards have a value  of 10. All other
cards have a value the same as its pip value.

Before a hand begins, you must place a bet. The minimum bet is $5, 
the maximum bet is $100.

Cards are then dealt. One to you, one to the dealer, a second to
you.

If the your first two cards are an ace and a "ten-card" (a picture card 
or 10), giving your hand a value of 21 in two cards, this is a natural 
or "blackjack". If you have a natural and the dealer does not, the 
dealer immediately pays you one and a half times (x1.5) the amount of 
your bet. If the dealer and another player both have naturals, the bet 
of that player is a stand-off (a tie), and the player takes back his 
chips.
""")
    print("\n" * 1)
    input("Press Enter to coninue...")
    print("""

Pg 2/3

You can decide on your turn whether to "hit" (ask for another card to 
get cloaser to 21) or "stand" (not ask for another card).

The dealer must continue to hit if her total is 16 or less.

Splitting Pairs - If your first two cards are of the same Rank e.g. two
Kings or two threes, you may choose to treat them as seperate hands. 
An equal amount to your initial bet must be placed as the bet on the 
second hand. You can then hit or stand seperately on each hand starting 
wit the first hand, then the second hand. If you split a pair of Aces,
you will be given one card for each hand only and may not hit again.
If a card with a value of ten is dealt to one of these split aces the 
payout is equal to the bet not the one and one-half to one (x1.5) as 
with Blackjack at any other time.

Doubling Down - Another option open to you is doubling your bet when
your first two cards are equal to either 9, 10 or 11. You can place a
bet equal to your initial bet and the dealer will give you a single 
card. With two fives, you have the option or splitting the pair or 
doubling down or just playing the hand. 

""")
    input("Press Enter to coninue...")
    print("""
	
Pg 3/3

The dealer does not have the option of Splitting Pairs or Doubling Down

Insurance - If the dealers first visible card is an Ace, you can place
a side bet of a minimum of $2.5 up to a maximum of half your initial
bet. If the dealer turns out to have Blackjack at the end of the round
you will be paid a two to one payoff (x2).

Settlement - A bet once paid is never returned. 
If you go bust you have lost your bet. 
If the dealer goes bust and you don't, you win.
If your total is higher than the dealers at the end, you win.
If there is a stand-off (your value is the same as teh dealers), no 
bets are paid out or collected and the bet rolls on to the next hand.

This is the popular six-deck game version as used in casinos. 
""")
    print("\n" * 5)
    input("Press enter to return to start menu")
    
    def titleArt():
        print("""
##########################################
#|======\ |       /=====\ /=====\ |     |#
#|      / |       |     | |       |    / #
#|=====<  |       |=====| |       |====  #
#|      | |       |     | |       |    \ #
#|======/ |=====| |     | \=====/ |     |#
#----------------------------------------#
#  I=======I  /=====\  /=====\  |     |  #
#      |      |     |  |        |    /   #
#      |      |=====|  |        |====    #
#      |      |     |  |        |    \   #
# \====/      |     |  \=====/  |     |  #
########################################## 
Programmed by James W Heath. 
""")
    titleArt()
    ans = input("Would you like to read the rules? type 'y' or just Enter to continue ")
    if ans == 'y':
        gameHelp()
        main()
    name = input("\nEnter your name to start: ")
    player = Player(name)
    
    def cls(): # Clears the screen to make it less cluttered
        print("\n" * 100)
    
    def displayInfo(): # Displays game info.
        cls()
        titleArt()
        player.showBank()
        player.showBet()
        dealer.showHand()
        player.showHand()
         
    def settlement(): # Wraps up the hand, pays out or takes money and starts new hand
        b = player.bet
        sb = player.secBet

        def bustCheck(): # Checks for bust hands
            if player.secHand: # If a second hand is present then does this
                if player.bust == True: # If 1st hand bust, does this
                    displayInfo()
                    input("\n1st hand is bust, ${} bet lost.".format(b))
                    dealer.bank += b
                    player.bet = []
                if player.secBust == True: # If 2nd hand bust, does this
                    displayInfo()
                    input("\n2nd hand is bust, ${} bet lost.".format(sb))
                    dealer.bank += sb
                    player.secBet = []
            else:
                if player.bust == True: # One hand only bust check
                    displayInfo()
                    input("\nHand is bust, ${} bet lost.".format(b))
                    dealer.bank += b
                    player.bet = []

        def standOffCheck(): # Checks for a tie in hand values
            if player.secHand: # If two hands in play
                if player.bust == False: # If player 1st hand is not bust
                    if player.handValue == 21 and dealer.handValue == 21: # Gives 1st bet back if stand off at 21
                        displayInfo()
                        input("\n1st hand is a Blackjack stand off. No payout. Bet collected.")
                        player.hand = []
                        player.handValue = []
                        player.bank += player.bet
                        player.bet = []
                    elif player.handValue == dealer.handValue: # 1st hand is stand off
                        displayInfo()
                        input("\n1st hand is a stand off, bet not paid out, bet not collected.")
                        player.hand = []
                        player.handValue = []
                if player.secBust == False: # If player 2nd hand is not bust
                    if player.secHandValue == 21 and dealer.handValue == 21: # Gives 2nd bet back if standoff at 21
                        displayInfo()
                        input("\n2nd hand is a Blackjack stand off. No payout. Bet collected.")
                        player.hand = []
                        player.handValue = []
                        player.bank += player.Secbet
                        player.secBet = []
                    elif player.secHandValue == dealer.handValue: # 2nd hand is stand off
                        displayInfo()
                        input("\n2nd hand is a stand off, bet not paid out, bet not collected.")
                        player.bet += sb
                        player.secBet = []
                        player.secHand = []
                        player.secHandValue = []            
            else: # For a single hand in play
                if player.bust == False:
                    if player.handValue == 21 and dealer.handValue == 21: # Gives bet back if stand off at 21
                        displayInfo()
                        input("\nBlackjack stand off. No payout. Bet collected.")
                        player.bank += player.bet
                        player.bet = []
                        reset()
                    elif player.handValue == dealer.handValue: # Hand is stand off
                        displayInfo()
                        input("\nStand off, bet not paid out, bet not collected.")
                        reset()

        def winCheck(): # Checks for winning hand and pays out accordingly
            if player.secHand: # Wincheck protocol for TWO HANDS
                if dealer.bust == True and player.bust == False: # If dealer bust but 1st hand not
                    displayInfo()
                    input("\n1st hand wins {}. Press enter.".format(b))
                    player.bank += b * 2
                    dealer.bank -= b
                    player.bet = []
                elif dealer.bust == False and player.bust == False: # If no one bust
                    if player.handValue > dealer.handValue: # 1st hand win
                        displayInfo()
                        input("\n1st hand wins ${} paid out! Press enter.".format(b))
                        player.bank += b * 2
                        dealer.bank -= b
                        player.bet = []
                    elif player.handValue < dealer.handValue: # 1st hand lose
                        displayInfo()
                        input("\n1st hand loses to dealer. ${} lost. Press enter.".format(b))
                        dealer.bank += b
                        player.bet = [] 
                if dealer.bust == True and player.secBust == False: # If dealer bust but 2nd hand not
                    displayInfo()
                    input("\n2nd hand wins {}. Press enter.".format(sb))
                    player.bank += sb * 2
                    dealer.bank -= b
                    player.secBet = []
                elif dealer.bust == False and player.secBust == False:
                    if player.secHandValue > dealer.handValue: #2nd hand win
                        displayInfo()
                        input("\n2nd hand wins ${} paid out! Press enter.".format(b))
                        player.bank += sb * 2
                        dealer.bank -= b
                        player.secBet = []
                    elif player.secHandValue < dealer.handValue: # 2nd hand loses
                        displayInfo()
                        input("\n2nd hand loses to dealer. ${} lost. Press enter.".format(b))
                        dealer.bank += sb 
                        player.secBet = []                           
            else: # Wincheck protocol for ONE HAND 
                if dealer.bust == True and player.bust == False: # If dealer bust but player not
                    displayInfo()
                    input("\nDealer is bust. ${} won. Press enter.".format(b))
                    player.bank += b * 2
                    dealer.bank -= b
                    player.bet = []                       
                elif dealer.bust == False and player.bust == False: # If no one bust value check
                    if player.handValue > dealer.handValue: # Hand wins
                        displayInfo()
                        input("\nYour hand wins ${} paid out! Press enter.".format(b))
                        player.bank += b * 2
                        dealer.bank -= b
                        player.bet = []
                    elif player.handValue < dealer.handValue: # Hand loses                      
                        displayInfo()
                        input("\nDealer wins. ${} lost. Press enter.".format(b))
                        dealer.bank += b
                        player.bet = []

        def insurancePay():
            x = player.sideBet * 3
            if player.sideBet:
                if dealer.handValue == 21:
                    displayInfo()
                    input("\nDealer has Blackjack, insurance pays ${}".format(x))
                    player.bank += x
                    dealer.bank -= x
                    player.sideBet = []
                else:
                    input("\nSide bet lost. Press enter.")
                    dealer.bank += player.sideBet
                    player.sideBet = []

        bustCheck()
        standOffCheck()
        winCheck()
        insurancePay()
        reset()
        gameStart()

    def reset():
        player.reset()
        dealer.reset()

    def naturalCheck(): # Seems to be working
        x = player.bet * 1.5
        displayInfo()
        if len(player.hand) == 2 and player.secHandValue == False: # So only works if two cards in hand and only first draw 
            if player.handValue == 21: # Skip to dealer draw and settle
                dealer.draw(deck)
                displayInfo() # This is here as it has the handValue calc method wrapped in it
                if dealer.handValue != 21: # If dealer hand not 21 then payout
                    input("\nNatural Blackjack, ${} bet won. Press enter.".format(x))
                    player.bank += player.bet + x
                    dealer.bank -= x
                    player.bet = []

                    reset()
                    gameStart()
        elif len(dealer.hand) == 2: # only works if two cards in dealer hand
            if player.handValue != 21 and dealer.handValue == 21:
                displayInfo()
                input("\nDealer has Natural Blackjack, ${} bet lost. Press enter.".format(player.bet))
                dealer.bank += player.bet
                player.bet = []
                reset()
                settlement()

    def play(): # The players play (1st)
        player.draw(deck)   # Player first card
        dealer.draw(deck)   # Dealer first card
        player.draw(deck)   # Player second card
        naturalCheck()      # Checks for natural blackjack
        player.splitPair()  # Split pair check and method
        player.doubleDown() # Double down check and method
        player.insurance()  # Insurance check and Method
        player.hit()        # player hit methods

    def dealerPlay(): # The dealers play (2nd)
        dealer.draw(deck)   # Dealer second card
        naturalCheck()
        dealer.hit()        # Dealer hit method
        
    def gameStart(): # Main game begin function
        while True:
            if player.bank < 5 and player.bet == []:
                input("\nSorry You're Broke, Game Over!!!")
                main()
            else:
                deck.newDeckCheck()
                player.makeBet()
                play()
                dealerPlay()
                settlement()
                    
    gameStart()            

if __name__ == "__main__":
    main()
