# BlackJack
Simple Python text based Black Jack game

#Comments
'''

- Play system. Essentialy a one player game.

What it needs to do:

Ask for a player name and start a game.

The gameplay:

1.) THE BET - players bet

2.) THE DEAL - dealer deals clockwise one card to each face up (dealer last), 
twice. Dealers second card is not shown (face down).
Check for naturals on players cards

3.) PLAY - players go in order. Choose to STAND or HIT. (player method)
IF goes BUST player is no longer in play and dealer collects bet.

4.) DEALERS PLAY - After all players have been served, dealer shows second card.
if dealer.handValue => 17:
    Dealer MUST STAND
if daler.handValue < 17:
    Dealer MUST HIT ('Soft Hand' applies but must stand on 17 regardless)

5.) SETTLEMENT - 
win check -  compare player and dealer handValues.
Highest handValue < 22 wins.
Check for stand-off (both player and dealer handValues same)
winnings = player.bet returned + player.bet amount from dealer 
IF blackjack - (player.handValue = 21) player.bet returned + 1.5 times
player.bet from the dealer

Things to consider:

- "Soft Hand" -

- 'Stand-off' Both player and dealer has blackjack. bets are returned.

- "Naturals" - check - if player start with 21 this is a 'natural'.
If dealer does not have a 'natural' then each player with a 'natural'
wins 1.5x his own bet. 
If dealer has a 'Natural' all players without a 'natural' lose their 
bet. If player and dealer both have 'naturals' it is a tie and player 
takes back bet.

- Betting - happens before cards are dealt. Min and max limits - more info.
(Create a self.bet and self.sideBet attributes for player class)

- Dealer class - attributes (hand, handValue), 
methods (check for a natural IF first card in hand (face up card) has
a value of ten or 11)

-Splitting pairs - if first to cards are of same value, player can Choose 
to treat them as two seperate hands. more info in rules. (player method)

- Doubling Down - when first two cards == 9 10 or 11 player can double
original bet. Dealer gives ONE card face down and not shown until the 
end of the hand. (player method)

- Insurance - When dealer face up hand value is == 11 (ace) player can
make a side bet of 1/2 their main bet that the dealers face down card is a
value ten card. If after all bets are placed the dealer then has blackjack,
players who bet are paid 2x their half bet. If players hand is not also 
blackjack players is lost. 
(player method)
'''

'''
done:
13.01.17 
    - side bet method added.
    - Betting: now can't bet more than bank with bet and sideBet methods
    - Clear_output method for later use. Both jupyter and terminal versions
    - doubleDown(): Working. checks for opertunity, asks player, sorts the betting. 
    - splitpair(): All working BUT damn IndexError : pop from empty list thing . Does seem to add a card to the hand all the 
    same though? checks for opertunity, asks player, makes a second hand.
    - Showsechand: Method to show if there is a second hand
14.01.17
    - copied over the dealer class methods.
    - Aces check is working!!!!!
15.01.17   
    - started ordering play methods
    - re-worked side bet mechanic
    - started winCheck function
    - added aceCheck to dealer methods
16.01.17
    - refined the showBet() method.
    - Fixed splitPair function :)
    - added displayInfo() function to most methods
    - fixed error in sechandvalue ace bust 
18.01.17
    - Minor play order changes.
    - WinCheck work. name changed to settlement()
    - global discard() function made to reset hands (later changed to reset() encompassing the player and dealer reset class 
    methods.
    - standOffCheck() complete
    - payOutCheck() started
    - bustCheck() complete
    - naturalCheck() working, could do with more testing
    - discard changed to reset() to facilitate bust attributes
    - bust attribute added to dealer and player
    - Added displayInfo infront of all prompts to try to fix appearing above info
    - betting error where money is returned only is fixed. Now payout properly
    - fixed double down drawing single card and going to dealer play section
    - created insurance payout
    - added a condition to the gameStart() function that requires the player.bank to be >= 5
    - start menu created with ACSII art and name entry player class instantiation
19.01.17
    - Corrected win check errors.
    - ported to geaney for terminal use
    - put in if __main__ == __name__: etc. business.
    - Seems to be working.
    - fixed double down betting bug
25.01.17
    - FOUND ERROR in stand off system. Need to loop back to game play start without making a new bet... (fixed 01.02.17) 
    answer 
    could be to put the stand off check inside another function?
    - Added a line to the makeBet() function that only asks if player bet == 0 to account for stand off game replay without 
    re-betting to play
    - found out that a stand off with blackjack player can take back bet. THEREFORE make it so in the game... 
    (fixed 02.02.17)
    - Added title art to displayInfo() looks pretty :)
01.02.17
    - Finished help menu at start screen.
    - FIXED - Natural blackjack bug (accepted more than 2 cards in hand....)
    - FIXED - stand off system and payouts.
    - Fixed insurance method "side bet lost" crash with simple addition of 'player.' to sideBet
02.02.17
    - Fixed crashing when bet and side bet inputs are not ints.
    - Minor changes to 'interface'.
    - Fixed blackjack stand off allowed to collect bet back.
    - Does seem to be finished for all intents and purposes. :D

30.03.17
 NEED FIXING - Found bug with being broke but game still asks to make a bet. 

15.05.17
    - Fixed broke but still asking for bet bug. Now resets back to start. Yay.
    - Fixed blackjack natural payout only paying out the 1.5x the bet and not the bet plus 1.5x the bet.

17.11.18
    - Broke game over. needs to check for not enough money in bank and not enough in bet from prev round. - Seems fixed now. Made check for list == []. May show as problem with bets of $2.5.
    - Found side bet on insurance wnot paying out when dealer has more than 2 cards in blackjack - Fix was to remove the 2 card requirement... Likely an oversight of mine mixing blackjack up with 'natural' blackjack. Still needs confirming fixed
    - Found broken handeling of split pairs where if the first hand gets a black jack it is recognised as a natural. I added a bit in the natural check function which checks that SecHandValue == False. Still need sconfirming fixed
    - Found bug where an ace insurance check happens on circumstances other than dealers first card- Fixed. made insurance check for only one card held.
    
TO DO:
    -Bug testing needed still on general betting etc.
    -Does the dealer still need to show cards if player is bust? Probably not.
    
TO DO (maybe?):
    pack up script into modules 
    
Fun ideas:
    -make a counter to show how many hands played. Fun to show at the end of a game too.
    -make a help line at the top of the terminal screen to give help and info on the state of play (added a help menu screen
    at help menu instead (01.02.17))
    -make a "Big Player" table with higher stakes to ask when a certain bank amount has been reached.
    -make a break the bank check that shows the player has bankrupt the casino.
    -ASCII art for the game over screen. 
    - A congratulations ASCII art for reaching a bank of >1000. 
    

'''
