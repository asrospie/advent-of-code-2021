import sys

def main():
    file = sys.argv[1]
    days = int(sys.argv[2])

    with open(file) as f:
        lines = f.readline()

    fish = [ int(x) for x in lines.split(',') ]

    for i in range(0, days):
        # print(f'DAY :: {i}')
        new_fish = 0

        for j, f in enumerate(fish):
            if f == 0:
                fish[j] = 6
                new_fish += 1
            else:
                fish[j] -= 1

        for j in range(0, new_fish):
            fish.append(8)

        print(fish)

    print(len(fish))

if __name__ == "__main__":
    main()