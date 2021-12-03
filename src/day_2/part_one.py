import sys

def main():
    file = sys.argv[1]

    with open(file) as f:
        lines = f.readlines()

    lines = [x.strip().split(' ') for x in lines]

    horizontal = 0
    depth = 0
    for line in lines:
        dr = line[0] # direction
        mag = int(line[1]) # magnitude
        if dr == 'forward':
            horizontal += mag 
        elif dr == 'down':
            depth += mag 
        elif dr == 'up':
            depth -= mag

    print(horizontal * depth)

if __name__ == "__main__":
    main()