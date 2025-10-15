def INPUT():
    M = int(input().strip())                 
    moves = list(map(int, input().split()))
    return M,moves
def who_win(who,board):
        wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)] 
        for a,b,c in wins:
            if board[a] == board[b] == board[c] == who:
                return True
        return False

def main():
    M,moves=INPUT()
    board = [0] * 9
    if M == 1:
        turn = 1  
    else: 
        turn=2                

    for i in range(5):
        board[moves[i] - 1] = turn
        if  turn == 2:
            turn = 1
        else:
            turn= 2         
    
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])

    if who_win(1,board):
        print("Player win")
    elif who_win(2,board):
        print("Computer win")
    else:
        print("Undecided")

main()
