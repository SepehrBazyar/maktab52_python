#Written by: Sepehr Bazyar
#This Code was Written in 2018 by Me for Quera

from HW8_07_Sudoku import Sudoku

global Ans, Arr
Arr = [[0 for j in range(9)]for i in range(9)]
Ans = [[0 for j in range(9)]for i in range(9)]

def Print():
    print()
    for i in range(9):
        Chp = [0 for i in range(9)]
        for j in range(9):
            Chp[j] = str(Ans[i][j])
        print(' '.join(Chp))

def Continue():
    for i in range(9):
        for j in range(9):
            if(Ans[i][j] == 0):
                return True
    return False

def Ofoghi(x, y):
    for i in range(9):
        if(Ans[x][i] == 0 and Arr[x][i].count(Ans[x][y]) != 0 and len(Arr[x][i]) > 1):
            Arr[x][i].remove(Ans[x][y])

def Amoodi(x, y):
    for i in range(9):
        if(Ans[i][y] == 0 and Arr[i][y].count(Ans[x][y]) != 0 and len(Arr[i][y]) > 1):
            Arr[i][y].remove(Ans[x][y])

def Moraba(x, y):
    if(0 <= x and x <= 2): p = 0
    elif(3 <= x and x <= 5): p = 3
    else: p = 6
    if(0 <= y and y <= 2): q = 0
    elif(3 <= y and y <= 5): q = 3
    else: q = 6
    i = p
    j = q
    while(i <= p + 2):
        while(j <= q + 2):
            if(Ans[i][j] == 0 and Arr[i][j].count(Ans[x][y]) != 0 and len(Arr[i][j]) > 1):
                Arr[i][j].remove(Ans[x][y])
            j += 1
        j = q
        i += 1

def Check():
    for i in range(9):
        for j in range(9):
            if(Ans[i][j] == 0 and len(Arr[i][j]) == 1):
                Arr[i][j] = Arr[i][j][0]
                Ans[i][j] = Arr[i][j]

def Ofoghi2():
    for i in range(9):
        for k in range(9):
            c = z = 0
            for j in range(9):
                if(Ans[i][j] == k + 1):
                    c = 0
                    break
                if(Ans[i][j] == 0 and Arr[i][j].count(k + 1) != 0):
                    z = j
                    c += 1
            if(c == 1):
                Ans[i][z] = k + 1
                Arr[i][z] = k + 1

def Amoodi2():
    for i in range(9):
        for k in range(9):
            c = z = 0
            for j in range(9):
                if(Ans[j][i] == k + 1):
                    c = 0
                    break
                if(Ans[j][i] == 0 and Arr[j][i].count(k + 1) != 0):
                    z = j
                    c += 1
            if(c == 1):
                Ans[z][i] = k + 1
                Arr[z][i] = k + 1

def Error():
    c = 0
    for i in range(9):
        for j in range(9):
            if(Ans[i][j] == Arr[i][j]):
                return False
            if(Ans[i][j] == 0):
                c += 1
    if(c > 0):
        return True
    return False

def Last():
    for i in range(9):
        for j in range(9):
            if not(Ans[i][j] == 0 or Arr[i][j] == -1):
                return False
    return True

sudoku = Sudoku()
print(sudoku)

array, S = sudoku.__repr__().split('\n')[4:15], []
for item in array:
    if item[1] != '-': S.append(' '.join(list(map(lambda x: x.strip(), item[2:23].split('|')))))

for i in range(9):
    S[i] = S[i].split(' ')
    for j in range(9):
        Ans[i][j] = int(S[i][j])
        if(S[i][j] == '0'):
            Arr[i][j] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        else:
            Arr[i][j] = int(S[i][j])

while Continue():
    for i in range(9):
        for j in range(9):
            if(Ans[i][j] != 0 and Arr[i][j] != -1):
                Ofoghi(i, j)
                Amoodi(i, j)
                Moraba(i, j)
                Arr[i][j] = -1
    Check()
    Ofoghi2()
    
    for i in range(9):
        for j in range(9):
            if(Ans[i][j] != 0 and Arr[i][j] != -1):
                Ofoghi(i, j)
                Amoodi(i, j)
                Moraba(i, j)
                Arr[i][j] = -1
    Check()
    Amoodi2()

    if Last():
        F = False
        for i in range(9):
            for j in range(9):
                if(Ans[i][j] == 0 and len(Arr[i][j]) > 0):
                    Arr[i][j] = Arr[i][j][0]
                    Ans[i][j] = Arr[i][j]
                    F = True
                    break
            if F:
                break

    if Error():
        print()
        print("Error")
        break

inp = input("Please Enter Key to Show Solution... ")

if not Continue():
    print("""
    <Sample Solution>
\n -----------------------
| {} {} {} | {} {} {} | {} {} {} |\n| {} {} {} | {} {} {} | {} {} {} |\n| {} {} {} | {} {} {} | {} {} {} |
|-----------------------|
| {} {} {} | {} {} {} | {} {} {} |\n| {} {} {} | {} {} {} | {} {} {} |\n| {} {} {} | {} {} {} | {} {} {} |
|-----------------------|
| {} {} {} | {} {} {} | {} {} {} |\n| {} {} {} | {} {} {} | {} {} {} |\n| {} {} {} | {} {} {} | {} {} {} |
 -----------------------
""".format(*Ans[0], *Ans[1], *Ans[2], *Ans[3], *Ans[4], *Ans[5], *Ans[6], *Ans[7], *Ans[8]))
