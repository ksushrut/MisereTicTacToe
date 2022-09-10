#!/usr/bin/python
def check(square):
    if(square[1]==square[2] and square[2]==square[3]):  #top row
        return -1
    elif(square[4]==square[5] and square[5]==square[6]):  #middle row
        return -1
    elif(square[7]==square[8] and square[8]==square[9]):  #bottom row
        return -1
    elif(square[1]==square[4] and square[4]==square[7]):  #left column
        return -1
    elif(square[2]==square[5] and square[5]==square[8]):  #middle column
        return -1
    elif(square[3]==square[6] and square[6]==square[9]):  #left column
        return -1
    elif(square[1]==square[5] and square[5]==square[9]):  #top row
        return -1
    elif(square[3]==square[5] and square[5]==square[7]):  #top row
        return -1
    elif(square[1]!='1' and square[2]!='2' and square[3]!='3' and
    square[4]!='4' and square[5]!='5' and square[6]!='6' and
    square[7]!='7' and square[8]!='8' and square[9]!='9'):  #check if game is going on
        return 0
    else:                                                   #check if stalemate
        return 1

def board(square):
    
    print("     |     |     ");
    print(" ",square[1], " | ",square[2]," | ", square[3])
    print("_____|_____|_____");
    print("     |     |     ");
    print(" ",square[4]," | ",square[5]," | ", square[6])
    print("_____|_____|_____");
    print("     |     |     ");
    print(" ",square[7]," | ",square[8]," | ", square[9])
    print("     |     |     ");

def main():
    print('\t***Tic Tac Toe***')
    print("Player 1 (X)  -  Player 2 (O)\n");
    square=['null','1','2','3','4','5','6','7','8','9']     #square list maintains record of board
    player=1
    i=1
    while(i==1):
        board(square)                                       #display the board
        if(player%2 ==1):                                   #assign player turn by turn
            player=1
        else:
            player=2
        print("Player ",player," turn")         
        choice = int(input('Enter board square:'))          #input square number
        if(player==1):                                      #assign X or O as per the player
            mark='X'    
        else:
            mark='O'
        if(choice==1 and square[1]=='1'):
            square[1]=mark
        elif(choice==2 and square[2]=='2'):
            square[2]=mark
        elif(choice==3 and square[3]=='3'):
            square[3]=mark
        elif(choice==4 and square[4]=='4'):
            square[4]=mark
        elif(choice==5 and square[5]=='5'):
            square[5]=mark
        elif(choice==6 and square[6]=='6'):
            square[6]=mark
        elif(choice==7 and square[7]=='7'):
            square[7]=mark
        elif(choice==8 and square[8]=='8'):
            square[8]=mark
        elif(choice==9 and square[9]=='9'):
            square[9]=mark
        else:
            print("Invalid move")
            player-=1
        i=check(square)
        if(i==-1):
            break
        else:
            player+=1
    board(square)
    if(i==0):
        print("Game draw")
    if(i==-1):
        print("Player ",player,"lost")

if __name__=='__main__':
    main()
