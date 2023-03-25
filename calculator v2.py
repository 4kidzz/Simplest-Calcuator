w = 0

def calc():

    global w

    if w < 1:
        print("\nWelcome to the simplest calculator!\n")
    
    try:
        x = int(input("Your first number: "))
        z = input("Your action: ")
        y = int(input("Your Second number: "))

    except ValueError:
        print('\nPlease enter only one digit in each number and nothing else!\n')
        w += 1
        calc()

    if z == "+":
        print("\nYour equation:", x + y)

    elif z == "-":
        print("\nYour equation:", x - y)

    elif z == "*":
        print("\nYour equation:", x * y)

    elif z == "/" or z == ":":
        if y == 0:
            print('\nYou can't divide by zero!" "\n")
            w += 1
            calc()
            
        elif y != 0:
            print('\nour equation:", x / y)

    elif z == "%":
        print('\nYour equation:", x % y)

    else:
        print('\nPlease enter only one action and nothing else!')
        print('\nFor example: "*", "/", "+", "-", "%"' "\n")
        w += 1
        calc()
        
