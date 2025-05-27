#AP CREATE PROJECT
#Felix Bosch

#Initialize

import random
import time #https://docs.python.org/3/library/time.html

suits = ["Spades", "Diamonds", "Hearts", "Clubs"]
numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
dictionary = {"2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9, "10" : 10, "Jack" : 10, "Queen" : 10, "King" : 10, "Ace" : 11} # https://stackoverflow.com/questions/14792562/assigning-integers-to-strings

#Functions

def createdeck():
    global deck
    deck = []
    for suit in suits:
        for number in numbers:
            deck.append((number, suit))
    return deck

def shuffledeck():
    random.shuffle(deck)
    return deck

def handvalue(hand):
    total = 0
    aces = 0
    i = 0
    while i < len(hand):
        card = hand[i][0]
        total = total + dictionary[card]
        if card == "Ace":
            aces = aces + 1
        i = i + 1
    while total > 21 and aces > 0:
        total = total - 10
        aces = aces - 1
    return total

def showhand(name, hand):
    if len(hand) == 0:
        print(name + "'s hand: (empty)")
        return
    result = name + "'s hand: " + hand[0][0] + " of " + hand[0][1]
    i = 1
    while i < len(hand):
        result = result + ", " + hand[i][0] + " of " + hand[i][1]
        i = i + 1
    print(result)

def playblackjack():
    print(" ====== Welcome to the Blackjack Machine ====== ")
    while True:
        createdeck()
        shuffledeck()
        playerhand = [deck.pop(), deck.pop()]
        dealerhand = [deck.pop(), deck.pop()]
        print("")
        showhand("Player", playerhand)
        print("Player's hand value: " + str(handvalue(playerhand)))
        print("")
        print("Dealer's hand: [Hidden], " + dealerhand[1][0] + " of " + dealerhand[1][1])
        print("Dealer's hand value: " + str(handvalue(dealerhand)))
        print("")

        playerbust = False
        while handvalue(playerhand) < 21:
            move = input("Would you like to hit or stand: ").lower()
            print("")
            if move == "hit":
                playerhand.append(deck.pop())
                showhand("Player", playerhand)
                print("Player's hand value: " + str(handvalue(playerhand)))
                print("")
                if handvalue(playerhand) > 21:
                    print("Bust! Player lost.")
                    playerbust = True
                    break
            elif move == "stand":
                break

        if not playerbust:
            print("Dealer's turn...")
            showhand("Dealer", dealerhand)
            print("")
            while handvalue(dealerhand) < 17:
                print("Dealer is below 17! Dealer draws.")
                print("")
                dealerhand.append(deck.pop())
                showhand("Dealer", dealerhand)
                print("Dealer's hand value: " + str(handvalue(dealerhand)))
                print("")
                time.sleep(2)

            print("Moment of truth...")
            print("")
            showhand("Player", playerhand)
            print("Player's hand value: " + str(handvalue(playerhand)))
            print("")
            showhand("Dealer", dealerhand)
            print("Dealer's hand value: " + str(handvalue(dealerhand)))

            playertotal = handvalue(playerhand)
            dealertotal = handvalue(dealerhand)

            if dealertotal > 21 or playertotal > dealertotal:
                print("")
                print("Player wins!")
            elif playertotal < dealertotal:
                print("")
                print("Dealer wins. Player lost!")
            else:
                print("")
                print("Push!")

        print("")
        again = input("Would you like to play again? (yes/no): ").lower()
        if again == "yes":
            print("Good luck!")
            deck.clear()
        else:
            print("Thank you for playing blackjack!")
            break

#Main
playblackjack()
