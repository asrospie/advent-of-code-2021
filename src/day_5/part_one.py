import sys

def print_board(board):
    for row in board:
        builder = ''
        for val in row:
            if val == 0:
                builder += '.'
                continue
            builder += str(val)
        print(builder)

def draw_lines(board, coords):
    for coord in coords:
        pos_one, pos_two = coord
        x1, y1 = pos_one
        x2, y2 = pos_two

        if x1 != x2 and y1 != y2:
            continue
    
        max_x = max([x1, x2])
        min_x = min([x1, x2])
        max_y = max([y1, y2])
        min_y = min([y1, y2])

        if y1 == y2:
            for x in range(min_x, max_x + 1):
                board[y1][x] += 1
        if x1 == x2:
            for y in range(min_y, max_y + 1):
                board[y][x1] += 1
    return board

def main():
    file = sys.argv[1]

    with open(file) as f:
        lines = f.readlines()
    
    coords = []
    x_vals = []
    y_vals = []
    for line in lines:
        cleaned = line.strip().split(' ')

        split_one = cleaned[0].split(',')
        x_1 = int(split_one[0])
        y_1 = int(split_one[1])
        x_vals.append(x_1)
        y_vals.append(y_1)
        pos_one = (x_1, y_1)

        split_two = cleaned[2].split(',')
        x_2 = int(split_two[0])
        y_2 = int(split_two[1])
        x_vals.append(x_2)
        y_vals.append(y_2)
        pos_two = (x_2, y_2)
        coords.append((pos_one, pos_two))


    max_y = max(y_vals)
    max_x = max(x_vals)
    board = [ [ 0 for x in range(0, max_x + 1) ] for y in range(0, max_y + 1) ]

    vents = draw_lines(board, coords)
    points = 0
    for row in vents:
        for val in row:
            if val >= 2:
                points += 1

    print(points)
if __name__ == "__main__":
    main()