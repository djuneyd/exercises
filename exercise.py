board = [["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

string = 0
num = 0
numvalue = 0
answer = True
pre = []
squares = []
columns = []


#division into squares
for k in range(3):
        for d in range(3):
                for i in range(3):
                        for j in range(3):
                                pre.append(board[string][num])
                                num += 1
                        string += 1
                        num = numvalue
                squares.append(pre)
                pre = []
        string = 0
        numvalue += 3
        num = numvalue

#division into columns
for i in range(9):
        for j in range(9):
                pre.append(board[j][i])
        columns.append(pre)
        pre = []

#logic
for i in range(9):
        if len(set(board[i])) == (len(board[i]) - board[i].count(".") + 1) and len(set(squares[i])) == (len(squares[i]) - squares[i].count(".") + 1) and len(set(columns[i])) == (len(columns[i]) - columns[i].count(".") + 1):
                continue
        else:
                answer = False
                break