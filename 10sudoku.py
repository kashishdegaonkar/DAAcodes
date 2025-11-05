def solve(board):
    for i in range(9):
        for j in range(9):
            if board[i][j]==0:
                for k in range(1,10):
                    if valid(board,i,j,k):
                        board[i][j]=k
                        if solve(board): return True
                        board[i][j]=0
                return False
    return True

def valid(b,r,c,k):
    for x in range(9):
        if b[r][x]==k or b[x][c]==k: return False
    sr=(r//3)*3; sc=(c//3)*3
    for i in range(sr,sr+3):
        for j in range(sc,sc+3):
            if b[i][j]==k: return False
    return True

board=[[0]*9 for _ in range(9)]
solve(board)
print("Solved Sudoku:")
for r in board: print(r)