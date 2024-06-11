import random
print("WELCOME TO TIC-TAC-TOE")
print("----------------------")
Numbers = [1,2,3,4,5,6,7,8,9]
gameboard = [[1,2,3],[4,5,6],[7,8,9]]
rows = 3
cols = 3
choices = ['X','O']
choice = ''
while choice not in choices:
    choice = input("'X' or 'O': ").upper()
    if (choice == 'X'):
        cpuchoice = 'O'
    elif (choice == 'O'):
        cpuchoice = 'X'
    else:
        print("Invalid choice, try again.")
                        


def print_gameboard():
    for i in range(rows):
        print("\n|---|---|---|")
        print("|", end = "")
        for j in range(cols):
            print("", gameboard[i][j], end = " |")
    print("\n|---|---|---|")

def modifyArray(num,turn):
    num -= 1
    if num in [0,1,2]:
        gameboard[0][num] = turn
    elif num in [3,4,5]:
        gameboard[1][num - 3] = turn
    elif num in [6,7,8]:
        gameboard[2][num - 6] = turn

### function for checking winner
        
def CheckWinner(gameboard,choice):
    if choice == 'X':
        cpuchoice = 'O'
    else:
        cpuchoice = 'X'
    ### X axis
    for i in range(cols):
        if gameboard[i][0] == choice and gameboard[i][1] == choice and gameboard[i][2] == choice:
            print("CONGRATS, You have won!")
            return choice
        elif gameboard[i][0] == cpuchoice and gameboard[i][1] == cpuchoice and gameboard[i][2] == cpuchoice:
            print("OOPS! Computer has won.")
            return cpuchoice
    ### Y axis
    for j in range(rows):
        if gameboard[0][j] == choice and gameboard[1][j] == choice and gameboard[2][j] == choice:
             print("CONGRATS, You have won!")
             return choice
        elif gameboard[0][j] == cpuchoice and gameboard[1][j] == cpuchoice and gameboard[2][j] == cpuchoice:
             print("OOPS! Computer has won.")
             return cpuchoice
    ### Cross wins
    if(gameboard[0][0] == choice and gameboard[1][1] == choice and gameboard[2][2] == choice):
        print("CONGRATS, You have won!")
        return choice
    elif(gameboard[0][0] == cpuchoice and gameboard[1][1] == cpuchoice and gameboard[2][2] == cpuchoice):
        print("OOPS! Computer has won.")
        return cpuchoice
    elif(gameboard[0][2] == choice and gameboard[1][1] == choice and gameboard[2][0] == choice):
        print("CONGRATS, You have won!")
        return choice
    elif(gameboard[0][2] == cpuchoice and gameboard[1][1] == cpuchoice and gameboard[2][0] == cpuchoice):
        print("OOPS! Computer has won.")
        return cpuchoice
    else:
        return "N"

leaveloop = False
turncount = 0

while(leaveloop == False):
    ### Player turn
    if(turncount % 2 == 0):
        print_gameboard()
        numberpicked = int(input("\nChoose a number [1-9]: "))
        if (numberpicked >= 1 or numberpicked <= 9):
            modifyArray(numberpicked, choice)
            Numbers.remove(numberpicked)
        else:
            print("Invalid input. Please try again.")
        turncount += 1
    ### computer's turn
    else:
        while (True):
            cpu = random.choice(Numbers)
            print("\nCPUchoice: ", cpu)
            if (cpu in Numbers):
                modifyArray(cpu,cpuchoice)
                Numbers.remove(cpu)
                turncount += 1
                break
    winner = CheckWinner(gameboard,choice)
    if (winner != "N"):
        print("\nGame Over ! Thank you for playing.")
        break
            
            
             
            
                  
                  

                  
                  
                  
        
        
