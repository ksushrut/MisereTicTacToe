# MisereTicTacToe
Tic Tac Toe game with a slight twist

Tic Tac Toe is a game which we would have definitely played during our childhood. However, with a decent understanding of the game, the game turns out to be draw more often then not. Therefore, the Misere(which literally means misery) version of the game, involves changing the winning criteria. The person to score three in a row, loses. 
This idea was adapted from a Numberphile video: https://www.youtube.com/watch?v=ktPvjr1tiKk

check function: Takes parameter as the square or the board in the form of list
Return -1 if three in a row occur
Return 1 if the game is going on
Return 0 in case of a draw

board function: Takes parameter as the square or the board in the form of list
Displays the board

main function: Determines the result of the game between Player 1 and Player 2<br>
Algorithm:
1. Start with player 1. Input choice/square number for player 1. 
2. Update the matrix at the particular location in the list.
3. Give chance for player 2. Input choice/square number for player 2. 
4. Update the matrix at the particular location in the list.
5. Call the check function to see if the game has ended or not.
6. If not, goto step 1. If yes, check if draw or which player has lost.

