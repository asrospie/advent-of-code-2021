import os
import sys

def main():
    day_number = sys.argv[1]

    path = f'./src/day_{day_number}'
    os.system(f'mkdir {path}')
    os.system(f'cp template.py {path}/part_one.py')
    os.system(f'cp template.py {path}/part_two.py')
    os.system(f'touch {path}/example.txt')
    os.system(f'touch {path}/input.txt')


if __name__ == "__main__":
    main()