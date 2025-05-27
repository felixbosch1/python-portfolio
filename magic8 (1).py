#Felix Bosch
#Magic 8 ball
#Initizalize
import random
import time
magiclist = ["Yes, definitely.", "Ask again later.", "Don't count on it.", "Most likely.", "Outlook good.", "My sources say no.", "Yes, but only if you believe.", "Cannot predict now.", "Yes, but it's complicated.", "The stars are aligned.", "Signs point to yes.", "Try again after a while.", "Chances are slim.", "All signs point to no.", "You may rely on it."]
#Functions

#Main
print("Welcome to the magic 8 ball")
while True:
    try:
        yesno = input("Enter a yes or no question: ")
        end = yesno.endswith("?")
        if end == True:
            print("shake....")
            time.sleep(2)
            print("shake...")
            time.sleep(2)
            print("shake..")
            time.sleep(2)
            print(random.choice(magiclist))
            new = input("Would you like to ask another question (yes or no): ")
            if new == "no":
                print("Enjoy the rest of your day!")
                break

    except:
        print("ERROR")



