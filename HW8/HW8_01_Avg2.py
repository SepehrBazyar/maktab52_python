#Written by: Sepehr Bazyar
import argparse

if __name__ == '__main__': #just run when run this program and not imported into the other programs
    parser = argparse.ArgumentParser(description = "<Calculate Average>") #title of the help program
    parser.add_argument('-g', '--grades', metavar = "GRADES", action = 'store', #get grades of student
    type = int, nargs = '*', required = True, help = "Get Grades") #forcible values and nargs is * mean infinity
    parser.add_argument('-f', '--float', metavar = "FLOAT DIGITS", action = 'store', #set number of float digit
    type = int, default = 2, help = "Float Digits Average Result") #check type and default value if not passing
    args = parser.parse_args() #add defined arguments in above to the args parser

    average = sum(args.grades) / len(args.grades) #args.grades is a list contains grades student
    print(f"Average Result = {average:.{args.float}f}") #set number of float digits with F-String
