import random       #random module for randomly selecting the number
import rangefinder  #range finder for helping to generate range hint feature in this game
import sys

turns = 5               #The player has 5 turns 

"""
9-11 : The lines read the Rules.txt which contain rules about this game
"""
f = open("Rules.txt", "r")      
print(f.read())     
f.close()

"""Some constants to the game."""
range_hints = (15,10,5, 3)
low_range_hints = []
high_range_hints = []
num = random.randint(1 ,100)
hint_varible = 0 #So, the hint variable helps to access the ranges as the turns pass on.

"""Creating a list for low_range_hints and high_range_hints"""
for x in range_hints:
    y = rangefinder.limit_finder(num, x)
    low_range_hints.append(y[0])
    high_range_hints.append(y[1])


def check_less_0_or_greater_than_100(number):

    """Checks that the low_ranges and high_ranges doesn't exceed the limit of numbers set in this game 
    that are 1-100."""
    if number < 1:
        return 1
    elif number > 100:
        return 100
    else:
        return number

"""39-40: Checks that low and high ranges doesn't exceed 1 and 100 respectively."""
low_range_hints = list(map(check_less_0_or_greater_than_100, low_range_hints))
high_range_hints = list(map(check_less_0_or_greater_than_100, high_range_hints))

"""Game Loop """
while turns != 0 :
    
    try:    
        guess = int(input("Guess the number...\t>>>"))

        if guess == num:
            print(f"You won.\n{guess} is the right number.\n")
            break

        elif turns == 1 and guess != num:
            print("You Lose !!!")
            print(f"The number was {num}.")
        
        elif turns > 1 and guess != num:
            print(f"This time your were not able to make it up.")
            print(f"As a hint, the number lies between {low_range_hints[hint_varible]} and {high_range_hints[hint_varible]}.")
            print("Please try again !!!")     
        
        turns -= 1  
        hint_varible += 1

    except ValueError:

        print("Please type an natural number .")
        print("As an penalty, one turn has been deducted.")
        
        if turns == 0:
            print("You Lose !!!")
            print(f"The number was {num}.")
        
        elif turns > 1:
            print("Please try again!!!\n")
        
        turns -= 1


    except:
        print("An error occured...")
        continue

if __name__ == '__main__':
    consent = input("Enter q to exit\n>>>")
    if consent.lower() == 'q':
        sys.exit()
