#Written by: Sepehr Bazyar
from random import randint, sample #randint for random number [1, 9] and sample for empty cells
import logging #logging for write log in console when restart create table when cant trying...

logging.basicConfig(level = logging.INFO, format = '%(asctime)s - %(levelname)-10s - %(message)s') #debug for developer

class LevelError(Exception): pass #create desire exception for when get invalid input for level of sudoku table

class _Table:
    "_Table Class Create an Object one List 9 * 9 with Returned Values Method." #docstring
    def __init__(self): self.table = [[0 for row in range(9)] for column in range(9)]

    def get_column(self, column: int) -> list: return [self.table[row][column] for row in range(9)] #column etc table[i]

    def get_cells(self, row: int, column: int) -> list: #get a cells with index etc row or column writing table[i][j]
        result = []
        for i in range((row // 3) * 3, (row // 3) * 3 + 3): #find start point of cell: (0, 0), (0, 3), (0, 6), (3, 0), ...
            for j in range((column // 3) * 3, (column // 3) * 3 + 3): result.append(self.table[i][j])
        return result

    def __repr__(self) -> str: #represent string for print self object
        return """
 -----------------------
| {} {} {} | {} {} {} | {} {} {} |\n| {} {} {} | {} {} {} | {} {} {} |\n| {} {} {} | {} {} {} | {} {} {} |
|-----------------------|
| {} {} {} | {} {} {} | {} {} {} |\n| {} {} {} | {} {} {} | {} {} {} |\n| {} {} {} | {} {} {} | {} {} {} |
|-----------------------|
| {} {} {} | {} {} {} | {} {} {} |\n| {} {} {} | {} {} {} | {} {} {} |\n| {} {} {} | {} {} {} | {} {} {} |
 -----------------------
""".format(*self.table[0], *self.table[1], *self.table[2], *self.table[3], #here format method be easier than f-string
*self.table[4], *self.table[5], *self.table[6], *self.table[7], *self.table[8])

class Sudoku: #sudoku class has combination from table not inheritance because a sudoku game has one table object
    "Sudoku Class has Created a Sudoku Table in Different Levels that it's Validated." #docstring
    __Elements = {"Easy": (29, 34), "Medium": (35, 47), "Hard": (48, 53)} #this dict is a private class attribute
    def __init__(self, level = "Easy"): #default value is easy level
        self.level = level.strip().title() #normalize the level name
        try: self.element = randint(*self.__Elements[self.level]) #unpacking value of level for randint function
        except: raise LevelError("Sudoku Level Must be one of the Cases[Simple or Medium or Hard]") #raise my exception
        self._table, zeros = _Table(), [[0] * 9] #create a table for game with _Table class and zeros array start loop
        while [0] * 9 in zeros: #while to a row or column or cell contains just zero generate new number for table
            if __name__ == '__main__': logging.debug("Generated a Sudoku Table.") #just in this program for developer
            self._generator() #generate a random table with _generator method
            zeros = [self._table.table[row] for row in range(9)] #add all rows and other to check [0] * 9 in list
            zeros += [self._table.get_column(column) for column in range(9)] #list comprehension column function
            for row in range(0, 9, 3): #a loop to add all cells to zeros with rows and columns for next time loop
                for column in range(0, 9, 3): zeros += [self._table.get_cells(row, column)]

    @staticmethod #a staticmetod function to check repetitious numbers excepted the 0(more 1 zero it is assumed 1)
    def _checking(*args) -> bool: return 9 - max(0, args.count(0) - 1) == len(set(args))

    def _validate(self, row: int, column: int) -> bool: #get a row and column and check related number in table and check
        flag_row = self._checking(*self._table.table[row])
        flag_column = self._checking(*self._table.get_column(column))
        flag_cells = self._checking(*self._table.get_cells(row, column))
        return flag_row and flag_column and flag_cells #subscription row and column and cells for validate

    def _generator(self) -> _Table: #generate a random table to game so return _Table object
        empty, flag = sample(range(81), self.element), False #sample choose empty cell and flag in start is false
        for row in range(9):
            for column in range(9):
                self._table.table[row][column] = randint(1, 9) #write a random number between 1 to 9 in cell
                if not self._validate(row, column): #that mean _validate is False and confilict with other numbers
                    previous_value = self._table.table[row][column] #save startin number to check all 9 numbers
                    while not self._validate(row, column): #loop to change number to validated cell
                        self._table.table[row][column] = ((self._table.table[row][column] + 1) % 9) + 1 #next numbers
                        if self._table.table[row][column] == previous_value: #that mean end of 9 numbers not possible
                            flag = True #change flag condition to True for check entering to this block or no
                            break #exit of this while loop
                if flag: break #if run above part exit from inner for loop
            if flag: break #exit from main for loop and restart table later

        else: #if for loop not braek and end natural that mean creat a table now remove empty random cells
            for row in range(9):
                for column in range(9): #calculate cell number to check in list to remove or no
                    if row * 9 + column in empty: self._table.table[row][column] = 0

        if flag: self._table = _Table() #restart create table for agian random number because we confilcted

    def __repr__(self) -> str: #here add level name in center of table top with center method so use f-string
        return f"""
{f"<Sudoku {self.level} Level>".center(25)}
{self._table.__repr__()}"""

def finished(*args) -> bool: #check finish game with 0 in numbers or not
    array = []
    for item in args:
        for index in item:
            array.append(index)
    return 0 in array

print("Welcome to My Sudoku Game ^_^\t{© Seper Bazyar}\n") #console gaming part for user...
lvl = int(input("Please Selece Game Level:\n1. Easy\n2. Medium\n3. Hard\n\n0 for Quit Game\n>>> "))
if lvl:
    print(sudoku := Sudoku(level = "Easy" if lvl == 1 else ("Medium" if lvl == 2 else "Hard")))
    allowing = [[not bool(column) for column in row] for row in sudoku._table.table] #changeables
    print("(Whenever You want to Leave the Game Just Enter 0 in Inputs!)\n")
    while finished(*sudoku._table.table):
        row, column = int(input("Intended  Row   Number: ")), int(input("Intended Column Number: "))
        if row and column:
            row -= 1; column -= 1
            if allowing[row][column]:
                num = int(input("\nWhat Number Replaced? "))
                pre, sudoku._table.table[row][column] = sudoku._table.table[row][column], num
                if not sudoku._validate(row, column):
                    sudoku._table.table[row][column] = pre
                    print("\nYou Can't Write this Number! Because Confilicted...")
            else: print("\nYou Can't Change this Number! Please Try Again...")
        else: break
        print(sudoku)
    else: print("Congratulations! You WIN! :))")
    print("\nGood Luck...")