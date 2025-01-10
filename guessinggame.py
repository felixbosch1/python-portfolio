#Guessing Game
#Felix Bosch
#Initiation
import random
#Functions
def guessinggame():
    print("Welcome to the guessing game!")
    diff = input("Please enter a level of difficulty you would like to try this guessing game at (easy, medium, hard): ")
    if diff == "easy":
        print("Welcome to the easy guessing game, you will be guessing a number from 1-10!")
        num = random.randint(1,10)
        guess = input("Enter your guess (1,10): ")
        if int(guess) > num:
            print("You guessed to high!")
            guess = input("Enter your guess (1,10): ")
            if int(guess) > num:
                print("You guessed to high!")
                guess = input("Enter your guess (1,10): ")
                if int(guess) == num:
                    print("You guessed it!")
                    playagain = input("Would you like to play again? if yes, enter yes: ")
                    if playagain == "yes":
                        guessinggame()
                    else:
                        print("Have a great rest of your day.")
                elif int(guess) != num:
                    print("You have lost.")
                    playagain = input("Would you like to play again? if yes, enter yes: ")
                    if playagain == "yes":
                        guessinggame()
                    else:
                        print("Have a great rest of your day.")
                else:
                    print("Bad input")
                    playagain = input("Would you like to play again? if yes, enter yes: ")
                    if playagain == "yes":
                        guessinggame()
                    else:
                        print("Have a great rest of your day.")
            elif int(guess) < num:
                print("You guessed to low!")
                guess = input("Enter your guess (1,10): ")
                if int(guess) == num:
                    print("You guessed it!")
                    playagain = input("Would you like to play again? if yes, enter yes: ")
                    if playagain == "yes":
                        guessinggame()
                    else:
                        print("Have a great rest of your day.")
                elif int(guess) != num:
                    print("You have lost.")
                    playagain = input("Would you like to play again? if yes, enter yes: ")
                    if playagain == "yes":
                        guessinggame()
                    else:
                        print("Have a great rest of your day.")
                else:
                    print("Bad input")
                    playagain = input("Would you like to play again? if yes, enter yes: ")
                    if playagain == "yes":
                        guessinggame()
                    else:
                        print("Have a great rest of your day.")
            elif int(guess) == num:
                print("You guessed it!")
                playagain = input("Would you like to play again? if yes, enter yes: ")
                if playagain == "yes":
                    guessinggame()
                else:
                    print("Have a great rest of your day.")
            else:
                print("Bad input")
                playagain = input("Would you like to play again? if yes, enter yes: ")
                if playagain == "yes":
                    guessinggame()
                else:
                    print("Have a great rest of your day.")
        elif int(guess) < num:
            print("You guessed to low!")
            guess = input("Enter your guess (1,10): ")
            if int(guess) > num:
                print("You guessed to high!")
                guess = input("Enter your guess (1,10): ")
                if int(guess) == num:
                    print("You guessed it!")
                    playagain = input("Would you like to play again? if yes, enter yes: ")
                    if playagain == "yes":
                        guessinggame()
                    else:
                        print("Have a great rest of your day.")
                elif int(guess) != num:
                    print("You have lost.")
                    playagain = input("Would you like to play again? if yes, enter yes: ")
                    if playagain == "yes":
                        guessinggame()
                    else:
                        print("Have a great rest of your day.")
                else:
                    print("Bad input")
                    playagain = input("Would you like to play again? if yes, enter yes: ")
                    if playagain == "yes":
                        guessinggame()
                    else:
                        print("Have a great rest of your day.")
            elif int(guess) < num:
                print("You guessed to low!")
                guess = input("Enter your guess (1,10): ")
                if int(guess) == num:
                    print("You guessed it!")
                    playagain = input("Would you like to play again? if yes, enter yes: ")
                    if playagain == "yes":
                        guessinggame()
                    else:
                        print("Have a great rest of your day.")
                elif int(guess) != num:
                    print("You have lost.")
                    playagain = input("Would you like to play again? if yes, enter yes: ")
                    if playagain == "yes":
                        guessinggame()
                    else:
                        print("Have a great rest of your day.")
                else:
                    print("Bad input")
                    playagain = input("Would you like to play again? if yes, enter yes: ")
                    if playagain == "yes":
                        guessinggame()
                    else:
                        print("Have a great rest of your day.")
            elif int(guess) == num:
                print("You guessed it!")
                playagain = input("Would you like to play again? if yes, enter yes: ")
                if playagain == "yes":
                    guessinggame()
                else:
                    print("Have a great rest of your day.")
            else:
                print("Bad input")
                playagain = input("Would you like to play again? if yes, enter yes: ")
                if playagain == "yes":
                    guessinggame()
                else:
                    print("Have a great rest of your day.")
        elif int(guess) == num:
            print("You guessed it!")
            playagain = input("Would you like to play again? if yes, enter yes: ")
            if playagain == "yes":
                guessinggame()
            else:
                print("Have a great rest of your day.")
        else:
            print("Bad input")
            playagain = input("Would you like to play again? if yes, enter yes: ")
            if playagain == "yes":
                guessinggame()
            else:
                print("Have a great rest of your day.")
    elif diff == "medium":
        print("Welcome to the mediun guessing game, you will be guessing a number from 1-50!")
        num = random.randint(1,50)
        guess = input("Enter your guess (1,50): ")
        if int(guess) > num:
            print("You guessed to high!")
            guess = input("Enter your guess (1,50): ")
            if int(guess) > num:
                print("You guessed to high!")
                guess = input("Enter your guess (1,50): ")
                if int(guess) == num:
                    print("You guessed it!")
                    playagain = input("Would you like to play again? if yes, enter yes: ")
                    if playagain == "yes":
                        guessinggame()
                    else:
                        print("Have a great rest of your day.")
                elif int(guess) != num:
                    print("You have lost.")
                    playagain = input("Would you like to play again? if yes, enter yes: ")
                    if playagain == "yes":
                        guessinggame()
                    else:
                        print("Have a great rest of your day.")
                else:
                    print("Bad input")
                    playagain = input("Would you like to play again? if yes, enter yes: ")
                    if playagain == "yes":
                        guessinggame()
                    else:
                        print("Have a great rest of your day.")
            elif int(guess) < num:
                print("You guessed to low!")
                guess = input("Enter your guess (1,50): ")
                if int(guess) == num:
                    print("You guessed it!")
                    playagain = input("Would you like to play again? if yes, enter yes: ")
                    if playagain == "yes":
                        guessinggame()
                    else:
                        print("Have a great rest of your day.")
                elif int(guess) != num:
                    print("You have lost.")
                    playagain = input("Would you like to play again? if yes, enter yes: ")
                    if playagain == "yes":
                        guessinggame()
                    else:
                        print("Have a great rest of your day.")
                else:
                    print("Bad input")
                    playagain = input("Would you like to play again? if yes, enter yes: ")
                    if playagain == "yes":
                        guessinggame()
                    else:
                        print("Have a great rest of your day.")
            elif int(guess) == num:
                print("You guessed it!")
                playagain = input("Would you like to play again? if yes, enter yes: ")
                if playagain == "yes":
                    guessinggame()
                else:
                    print("Have a great rest of your day.")
            else:
                print("Bad input")
                playagain = input("Would you like to play again? if yes, enter yes: ")
                if playagain == "yes":
                    guessinggame()
                else:
                    print("Have a great rest of your day.")
        elif int(guess) < num:
            print("You guessed to low!")
            guess = input("Enter your guess (1,50): ")
            if int(guess) > num:
                print("You guessed to high!")
                guess = input("Enter your guess (1,50): ")
                if int(guess) == num:
                    print("You guessed it!")
                    playagain = input("Would you like to play again? if yes, enter yes: ")
                    if playagain == "yes":
                        guessinggame()
                    else:
                        print("Have a great rest of your day.")
                elif int(guess) != num:
                    print("You have lost.")
                    playagain = input("Would you like to play again? if yes, enter yes: ")
                    if playagain == "yes":
                        guessinggame()
                    else:
                        print("Have a great rest of your day.")
                else:
                    print("Bad input")
                    playagain = input("Would you like to play again? if yes, enter yes: ")
                    if playagain == "yes":
                        guessinggame()
                    else:
                        print("Have a great rest of your day.")
            elif int(guess) < num:
                print("You guessed to low!")
                guess = input("Enter your guess (1,50): ")
                if int(guess) == num:
                    print("You guessed it!")
                    playagain = input("Would you like to play again? if yes, enter yes: ")
                    if playagain == "yes":
                        guessinggame()
                    else:
                        print("Have a great rest of your day.")
                elif int(guess) != num:
                    print("You have lost.")
                    playagain = input("Would you like to play again? if yes, enter yes: ")
                    if playagain == "yes":
                        guessinggame()
                    else:
                        print("Have a great rest of your day.")
                else:
                    print("Bad input")
                    playagain = input("Would you like to play again? if yes, enter yes: ")
                    if playagain == "yes":
                        guessinggame()
                    else:
                        print("Have a great rest of your day.")
            elif int(guess) == num:
                print("You guessed it!")
                playagain = input("Would you like to play again? if yes, enter yes: ")
                if playagain == "yes":
                    guessinggame()
                else:
                    print("Have a great rest of your day.")
            else:
                print("Bad input")
                playagain = input("Would you like to play again? if yes, enter yes: ")
                if playagain == "yes":
                    guessinggame()
                else:
                    print("Have a great rest of your day.")
        elif int(guess) == num:
            print("You guessed it!")
            playagain = input("Would you like to play again? if yes, enter yes: ")
            if playagain == "yes":
                guessinggame()
            else:
                print("Have a great rest of your day.")
        else:
            print("Bad input")
            playagain = input("Would you like to play again? if yes, enter yes: ")
            if playagain == "yes":
                guessinggame()
            else:
                print("Have a great rest of your day.")
    elif diff == "hard":
        print("Welcome to the hard guessing game, you will be guessing a number from 1-100!")
        num = random.randint(1,100)
        guess = input("Enter your guess (1,100): ")
        if int(guess) > num:
            print("You guessed to high!")
            guess = input("Enter your guess (1,100): ")
            if int(guess) > num:
                print("You guessed to high!")
                guess = input("Enter your guess (1,100): ")
                if int(guess) == num:
                    print("You guessed it!")
                    playagain = input("Would you like to play again? if yes, enter yes: ")
                    if playagain == "yes":
                        guessinggame()
                    else:
                        print("Have a great rest of your day.")
                elif int(guess) != num:
                    print("You have lost.")
                    playagain = input("Would you like to play again? if yes, enter yes: ")
                    if playagain == "yes":
                        guessinggame()
                    else:
                        print("Have a great rest of your day.")
                else:
                    print("Bad input")
                    playagain = input("Would you like to play again? if yes, enter yes: ")
                    if playagain == "yes":
                        guessinggame()
                    else:
                        print("Have a great rest of your day.")
            elif int(guess) < num:
                print("You guessed to low!")
                guess = input("Enter your guess (1,100): ")
                if int(guess) == num:
                    print("You guessed it!")
                    playagain = input("Would you like to play again? if yes, enter yes: ")
                    if playagain == "yes":
                        guessinggame()
                    else:
                        print("Have a great rest of your day.")
                elif int(guess) != num:
                    print("You have lost.")
                    playagain = input("Would you like to play again? if yes, enter yes: ")
                    if playagain == "yes":
                        guessinggame()
                    else:
                        print("Have a great rest of your day.")
                else:
                    print("Bad input")
                    playagain = input("Would you like to play again? if yes, enter yes: ")
                    if playagain == "yes":
                        guessinggame()
                    else:
                        print("Have a great rest of your day.")
            elif int(guess) == num:
                print("You guessed it!")
                playagain = input("Would you like to play again? if yes, enter yes: ")
                if playagain == "yes":
                    guessinggame()
                else:
                    print("Have a great rest of your day.")
            else:
                print("Bad input")
                playagain = input("Would you like to play again? if yes, enter yes: ")
                if playagain == "yes":
                    guessinggame()
                else:
                    print("Have a great rest of your day.")
        elif int(guess) < num:
            print("You guessed to low!")
            guess = input("Enter your guess (1,100): ")
            if int(guess) > num:
                print("You guessed to high!")
                guess = input("Enter your guess (1,100): ")
                if int(guess) == num:
                    print("You guessed it!")
                    playagain = input("Would you like to play again? if yes, enter yes: ")
                    if playagain == "yes":
                        guessinggame()
                    else:
                        print("Have a great rest of your day.")
                elif int(guess) != num:
                    print("You have lost.")
                    playagain = input("Would you like to play again? if yes, enter yes: ")
                    if playagain == "yes":
                        guessinggame()
                    else:
                        print("Have a great rest of your day.")
                else:
                    print("Bad input")
                    playagain = input("Would you like to play again? if yes, enter yes: ")
                    if playagain == "yes":
                        guessinggame()
                    else:
                        print("Have a great rest of your day.")

            elif int(guess) < num:
                print("You guessed to low!")
                guess = input("Enter your guess (1,100): ")
                if int(guess) == num:
                    print("You guessed it!")
                    playagain = input("Would you like to play again? if yes, enter yes: ")
                    if playagain == "yes":
                        guessinggame()
                    else:
                        print("Have a great rest of your day.")
                elif int(guess) != num:
                    print("You have lost.")
                    playagain = input("Would you like to play again? if yes, enter yes: ")
                    if playagain == "yes":
                        guessinggame()
                    else:
                        print("Have a great rest of your day.")
                else:
                    print("Bad input")
                    playagain = input("Would you like to play again? if yes, enter yes: ")
                    if playagain == "yes":
                        guessinggame()
                    else:
                        print("Have a great rest of your day.")
            elif int(guess) == num:
                print("You guessed it!")
                playagain = input("Would you like to play again? if yes, enter yes: ")
                if playagain == "yes":
                    guessinggame()
                else:
                    print("Have a great rest of your day.")
        elif int(guess) == num:
            print("You guessed it!")
            playagain = input("Would you like to play again? if yes, enter yes: ")
            if playagain == "yes":
                guessinggame()
            else:
                print("Have a great rest of your day.")
        else:
            print("Bad input")
            playagain = input("Would you like to play again? if yes, enter yes: ")
            if playagain == "yes":
                guessinggame()
            else:
                print("Have a great rest of your day.")



#Main
guessinggame()
