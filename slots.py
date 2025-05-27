#Felix Bosch
#Slot Machine
#Initalization
import random
import time
global credits
credits = 100
symbols = ['♥', '♦', '♠', '♣', '☆', '7']
slot1 = '7'
slot2 = '7'
slot3 = '7'
#functions

#main
print(" ====== Welcome to the 3-Slot Machine ====== ")
print("Slot Machine Symbols: " + str(symbols))
print("You have " + str(credits) + " credits. Each spin costs 10 credits.")
print("Press 'S' to spin or 'Q' to quit.")
print("Credits: " + str(credits))
print("Current Slots: [" + slot1+ "] [" + slot2 + "] [" + slot3 + "]")
while True:
    try:
        sq = input("Spin the slots? (S/Q): ")
        sq = sq.capitalize()
        if sq == "S":
            time.sleep(1)
            print("Spinning...")
            time.sleep(1)
            slot1 = random.choice(symbols)
            slot2 = random.choice(symbols)
            slot3 = random.choice(symbols)
            if slot1 == slot2 == slot3 == '7':
                print("Congratulation! You won! Jackpot! All 7's!")
                print("Current Slots: [" + slot1+ "] [" + slot2 + "] [" + slot3 + "]")
                credits = credits + 200
                print("+200 credits earned.")
                print("Credits: " + str(credits))

            elif slot1 == slot2 == slot3:
                print("Congratulation! You won! With 3 matching!")
                print("Current Slots: [" + slot1+ "] [" + slot2 + "] [" + slot3 + "]")
                credits = credits + 50
                print("+50 credits earned.")
                print("Credits: " + str(credits))

            elif slot1 == slot2 or slot1 == slot3 or slot2 == slot3:
                print("Congratulation! You won! With 2 matching!")
                print("Current Slots: [" + slot1+ "] [" + slot2 + "] [" + slot3 + "]")
                credits = credits + 20
                print("+20 credits earned.")
                print("Credits: " + str(credits))

            else:
                print("Sorry, no match this time.")
                print("Current Slots: [" + slot1+ "] [" + slot2 + "] [" + slot3 + "]")
                credits = credits - 10
                print("Credits: " + str(credits))
                if credits == 0:
                    print("""You have ran out of credits.
Would you like to add more credits (Y/N)""")
                    add = input("")
                    add = add.capitalize()
                    if add == "Y":
                        print("Your credits have been restocked!")
                        credits = 100
                        print("Credits: " + str(credits))
                    else:
                        print(" ====== Thank you for playing! ====== ")
                        print("Final Credits: " + str(credits))
                        break

        elif sq == "Q":
            print(" ====== Thank you for playing! ====== ")
            print("Final Credits: " + str(credits))
            break
        
    except:
        print("ERROR")



