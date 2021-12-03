import sys

def main():
    input_file = sys.argv[1]

    with open(input_file) as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        lines[i] = int(line.strip())

    group_sums = []
    for i, line in enumerate(lines):
        if i <= len(lines) - 3:
            group_sums.append(sum(lines[i:i + 3]))

    num_inc = 0
    for i, val in enumerate(group_sums):
        if i == 0:
            continue

        if val > group_sums[i - 1]:
            num_inc += 1

    print(num_inc)

    

if __name__ == "__main__":
    main()