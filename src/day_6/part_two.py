import sys

def main():
    file = sys.argv[1]

    with open(file) as f:
        line = f.readline().strip()

    init_fish = [ int(x) for x in line.split(',')]

    states = [ 0 for _ in range(0, 9) ]

    for fish in init_fish:
        states[fish] += 1

    for _ in range(0, 256):
        new_fish = states.pop(0)
        states.append(0)
        states[8] += new_fish
        states[6] += new_fish

    print(sum(states))

if __name__ == "__main__":
    main()