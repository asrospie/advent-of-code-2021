import sys

def num_of_increases(lines):
    num_inc = 0
    for i, line in enumerate(lines):
        if i == 0:
            continue

        if line > lines[i - 1]:
            num_inc += 1

    return num_inc

def main():
    input_file = sys.argv[1]

    # read input data
    with open('input.txt') as f:
        lines = f.readlines()

    # convert to int and remove white space
    for i, line in enumerate(lines):
        lines[i] = int(line.strip())

    print(num_of_increases(lines))

if __name__ == "__main__":
    main()