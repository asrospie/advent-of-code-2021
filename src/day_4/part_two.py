import sys

def check_col(board):
    cols = [ [board[j][i] for j in range(0, 5)] for i in range(0, 5) ]  

    solved = False
    for col in cols:
        if sum(col) == -5:
            solved = True

    if not solved:
        return -1

    total = 0
    for col in cols:
        for x in col:
            if x >= 0:
                total += x

    return total


def check_row(board):
    solved = False
    for row in board:
        if sum(row) == -5:
            solved = True

    if not solved:
        return -1 
    
    total = 0
    for row in board:
       for x in row:
           if x >= 0:
               total += x 

    return total

def mark_score(board, val):
    for i, line in enumerate(board):
        for j, num in enumerate(line):
            if num == val:
                board[i][j] = -1

def main():
    # Parse input
    file = sys.argv[1]

    with open(file) as f:
        lines = f.readlines()

    called = [int(x) for x in lines[0].split(',')]

    # Parse boards
    boards = []
    builder = []
    for i, line in enumerate(lines[2:]):
        if line == '\n':
            boards.append(builder)
            builder = []
            continue

        builder.append([int(x) for x in line.split()])

        if i + 1 == len(lines[2:]):
            boards.append(builder)


    solved_board_scores = [-1 for i in range(0, len(boards))]
    last_idx = -1
    for val in called:
        for i, board in enumerate(boards):
            if solved_board_scores[i] != -1:
                continue

            mark_score(board, val)
            col_score = check_col(board)

            if col_score >= 0:
                solved_board_scores[i] = col_score * val
                last_idx = i

            row_score = check_row(board)

            if row_score >= 0:
                solved_board_scores[i] = row_score * val
                last_idx = i

    print(solved_board_scores[last_idx])


if __name__ == "__main__":
    main()