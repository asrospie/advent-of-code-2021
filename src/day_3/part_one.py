import sys

def main():
    input_file = sys.argv[1]

    with open(input_file) as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        lines[i] = list(line.strip())

    # convert to ints
    # lines = [list(map(int, i)) for i in lines]

    # find most common
    gamma_list = []
    epsilon_list = []
    for i in range(0, len(lines[0])):
        one_count = 0
        zero_count = 0
        print('run')

        for j, line in enumerate(lines):
            if line[i] == '0':
                zero_count += 1
            else:
                one_count += 1
        # print(f'{i} :: 1 {one_count} :: 0 {zero_count}')
        if one_count > zero_count:
            gamma_list.append('1')
            epsilon_list.append('0')
        else:
            epsilon_list.append('1')
            gamma_list.append('0')
         
    epsilon_str = ''.join(epsilon_list)
    gamma_str = ''.join(gamma_list)


    epsilon = int(epsilon_str, 2)
    gamma = int(gamma_str, 2)
    
    print(epsilon * gamma)

if __name__ == "__main__":
    main()