import re

def is_it_possible(field): #"XXXOOOXXX" <= [str]
    print("", field[:3], "\n", field[3:6], "\n", field[6:])
    #
    #
    # TEST 1: Counting Pieces & Ex goes first
    # # # # #
    sumEx = field.count("X")
    sumOh = field.count("0")
    print(f"Xs: {sumEx}, 0s: {sumOh}")
    if sumOh > sumEx: print("More 0s than Xs/X plays first")
    if sumOh > sumEx: return False # Ex always play first / too many Os
    if sumEx - sumOh > 1: return False  #X has too many pieces, X either has exactly 1 or 0 pieces more
    #    
    #
    # TEST 2: Check win conditions, too many winners
    # # # # #
    wins = [ # only looking at X or 0, not the other or blanks
        "ooo......", #Horizontal win, top
        "...ooo...", #Horizontal win, mid
        "......ooo", #Horizontal win, bottom
        "o...o...o", #Diagonal win, L-R
        "..o.o.o..", #Diagonal win, R-L   ####
        "o..o..o..", #Vertical win, L
        ".o..o..o.", #Vertical win, mid
        "..o..o..o", #Vertical win, R
    ]
    
    
    checkEx = field.replace("X","o").replace("0", ".").replace("_", ".")
    winEx = 0 #counter 
    
    checkOh = field.replace("0", "o").replace("X", ".").replace("_", ".")
    winOh = 0
    #
    #
    # IF X/0 wins but has more pieces on the board the win-check FAILS! 
    # Loop over winning board index. For each 'o', check if a match on the actual gameboard... USE REGEX
    for win in wins: # iterate over each possible winning condition
        print("X", checkEx, "|", win, "|", "0", checkOh)
        winReg = str(win.replace(".","[o\.]{1}"))
        #print(win, "|")
        
        #if checkEx == winReg: #CHANGE!
        checkRegEx = re.search(str(winReg),str(checkEx))
        checkRegOh = re.search(str(winReg), str(checkOh))
        if checkRegEx:
            print("X won")
            winEx += 1
        if checkRegOh:
            print("0 won")
            winOh += 1
            
            
    print(winEx, winOh)
    if winEx > 0 and winOh > 0: return False #both sides CANNOT win
    if winEx > 2 or winOh > 2: return False # X/0 cannot have more than 2 winning conditions
    if winEx and sumOh >= sumEx: return False # if X wins, 0 must have 1 less piece
    if winOh and sumEx > sumOh: return False # if 0 wins, equal number of pieces on board
    #
    #
    #
    return True # GAME VALID
    #FIN # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    
    
"""
X/0 CAN win twice, if winning move is at intersection of 2 'ready lines'
    XXX
    ..X
    ..X
"""

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""
Task
Write a program that uses the image of the Tic-Tac-Toe field to determine whether this situation could have occurred as a result of playing with all the rules.
Recall that the game of "Tic-Tac-Toe" is played on a 3x3 field. Two players take turns. The first puts a cross, and the second – a zero. It is allowed to put a cross and a zero in any cell of the field that is not yet occupied. When one of the players puts three of his signs in the same horizontal, vertical or diagonal, or when all the cells of the field are occupied, the game ends.

Input/Output
Input: a 9-character string describing the playing field, the "_" symbol indicates an empty cell. It is guaranteed that the string contains only the characters "X", "0", "_".

Output: True if this situation can occur during a fair game according to the rules and False otherwise.

Examples

is_it_possible("XXX"+\
               "XXX"+\
               "XXX")    # Should return False

is_it_possible("0XX"+\
               "XX0"+\
               "00X")    # Should return True

is_it_possible("XXX"+\
               "0_0"+\
               "___")    # Should return True

is_it_possible("___"+\
               "___"+\
               "___")    # Should return True

is_it_possible("XXX"+\
               "000"+\
               "___")    # Should return False
               
               
"""
