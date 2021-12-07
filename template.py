import sys

def main():
    file = sys.argv[1]

    with open(file) as f:
        lines = f.readlines()

if __name__ == "__main__":
    main()