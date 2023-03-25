w = 0

def calc():

    global w

    if w < 1:
        print("\n" "Welcome to the simplest calculator!" "\n")
    
    try:
        x = int(input("Your first number: "))

        z = input("Your action: ")

        y = int(input("Your Second number: "))

    except ValueError:
        print("\n" "Please enter only one digit in each number and nothing else!" "\n")
        w += 1
        calc()

    if z == "+":
        print("\n" "Your equation:", x + y)

    elif z == "-":
        print("\n" "Your equation:", x - y)

    elif z == "*":
        print("\n" "Your equation:", x * y)

    elif z == "/" or z == ":":
        if y == 0:
            print("\n" "You can't divide by zero!" "\n")
            w += 1
            calc()
            
        elif y != 0:
            print("\n" "Your equation:", x / y)

    elif z == "%":
        print("\n" "Your equation:", x % y)

    else:
        print("\n" 'Please enter only one action and nothing else!')
        print("\n" 'For example: "*", "/", "+", "-", "%"' "\n")
        w += 1
        calc()
        
