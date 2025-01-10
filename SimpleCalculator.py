#Simple Calculator
#Felix Bosch

#Initiation

#Functions
def add(num1, num2):
    ans = num1 + num2
    print("Your answer is: " + str(ans))
def sub(num1, num2):
    ans = num1 - num2
    print("Your answer is: " + str(ans))
def div(num1, num2):
    ans = num1 / num2
    print("Your answer is: " + str(ans))
def mul(num1, num2):
    ans = num1 * num2
    print("Your answer is: " + str(ans))
def simplecalculator():
    print("Welcome Preschoolers to Simple Calculator!")
while True:
    print("Enter an operation: ")
    print("""1.Addition
    2.Subtraction
    3.Division
    4.Multiplication
    5.Quit""")
    operation = int(input("(1-5)Operation: "))
    if operation == 1:
        int1 = int(input("Enter your first number: "))
        int2 = int(input("Enter your second number: "))
        add(int1, int2)
    elif operation == 2:
        int1 = int(input("Enter your first number: "))
        int2 = int(input("Enter your second number: "))
        sub(int1, int2)
    elif operation == 3:
        int1 = int(input("Enter your first number: "))
        int2 = int(input("Enter your second number: "))
        div(int1, int2)
    elif operation == 4:
        int1 = int(input("Enter your first number: "))
        int2 = int(input("Enter your second number: "))
        mul(int1, int2)
    elif operation == 5:
        print("cya")
        break
    else:
        print("Wrong input")
#Main
simplecalculator()
