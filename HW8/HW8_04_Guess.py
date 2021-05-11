#Written by: Sepehr Bazyar
from random import randint as rand
import argparse

if __name__ == '__main__': #run just when run this program not import at other program
    parser = argparse.ArgumentParser(description = "<Guess Number Game>")
    parser.add_argument('-f', '--force', metavar = 'START', action = 'store', type = int,
    default = 0, help = 'Start of Point Number(Lower Bound)') #int number for start default value is 0
    parser.add_argument('-t', '--terminal', metavar = 'END', action = 'store', type = int,
    default = 100, help = 'End of Point Number(Upper Bound)') #int number for end default value is 100
    parser.add_argument('-g', '--game', metavar = 'TIMES', action = 'store', type = int,
    default = 5, help = 'Times of Game(Round for Guess Number)') #int number for round default value is 5
    args = parser.parse_args()

    if not args.force <= args.terminal: args.force, args.terminal = args.terminal, args.force #sort points number
    num = rand(args.force, args.terminal) #set random number in inputs range
    print(f"I Choose a Number in [{args.force}, {args.terminal}].\nNow You Guess in {args.game} Times... ^_^\n")
    for counter in range(args.game): #loop to counter < args.name
        x = input(f"{counter + 1}) Please Enter Your Guess -> ").strip() #strip for delete extra space and ...
        while not x.isnumeric(): #isnumeric string method check can cast to int and loop get valid input
            print("\nTry Again and Please be Careful in Enter Valid Number...\n")
            x = input(f"{counter + 1}) Please Enter Your Guess -> ").strip()
        x = int(x)
        if x < num: #user guess number less than my random number(print if not last round)
            if counter < args.game - 1: print("\nPlease Enter Higher Number For Next Round.\n")
        elif x > num: #user guess number greathar than my random number(print if not last round)
            if counter < args.game - 1: print("\nPlease Enter Lower Number For Next Round.\n")
        else: # x == num and finished the game
            print("\nYesss!! Exactly. You WIN :))")
            break
    else: print(f"\nOh Nooo!! You Lost... :((\nMy Number was {num}") #if not break and lose and say number
