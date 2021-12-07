import sys

def main():
    file = sys.argv[1]

    with open(file) as f:
        line = f.readline().strip()

    positions = [ int(x) for x in line.split(',') ]

    min_pos = min(positions)
    max_pos = max(positions)

    min_cost = 100000000
    for i in range(min_pos, max_pos + 1):
        running_cost = 0
        for p in positions:
            running_cost += abs(p - i)

        if running_cost < min_cost:
            min_cost = running_cost

    print(min_cost)

if __name__ == "__main__":
    main()