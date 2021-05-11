#Written by: Sepehr Bazyar
import sys

if __name__ == '__main__': #just run when run this program and not imported into the other programs
    summation, count = 0, 0
    for item in sys.argv: #check valid inputs and casting to float and add to calculated
        try: summation += float(item)
        except: pass
        else: count += 1
    try: average = summation / count
    except: print("Please be Careful in Entering the Scores...!") #if nothing valid input in sys.args
    else: print("Average Result =", int(average) if average.is_integer() else average) #for example 3.0 is 3
