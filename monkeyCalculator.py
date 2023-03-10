def calculateTime():
    
    # This first line is provided for you
    monkey_one = input("Is the first monkey smiling?:  ")
    monkey_two = input("Is the second monkey smiling?: ")

    if monkey_two == 'y' == monkey_one:
        print("Uh Oh! We're in trouble!")
    elif monkey_one == 'y':
        print("Yay! We're going to have a good day!")
    elif monkey_two == 'y':
        print("Yay! We're going to have a good day!")
    elif monkey_two == 'y' == monkey_one:
        print("Uh Oh! We're in trouble!")
    else:
        print("Uh Oh! We're in trouble!")
    # end assignment


## If you want to test locally run > python monkeyCalculator.py

if __name__ == "__main__":
    calculateTime()
    
