import sys

def solve_list(list, idx, val):
    # print(list)
    if len(list) == 1:
        print(list[0])
        return list[0]

    one_count = 0
    zero_count = 0
    for num in list:

        if num[idx] == '1':
            one_count += 1
        else:
            zero_count += 1

    val_check = ''
    if val == 'o':
        val_check = '1' if one_count >= zero_count else '0'
    else:
        val_check = '0' if zero_count <= one_count else '1'
    print(val_check)

    prune_list = [x for x in list if x[idx] == val_check]

    return solve_list(prune_list, idx + 1, val)

def main():
    input_file = sys.argv[1]

    with open(input_file) as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        lines[i] = list(line.strip())

    oxygen = solve_list(lines, 0, 'o')
    co2 = solve_list(lines, 0, 'c')

    o = int(''.join(oxygen), 2)
    c = int(''.join(co2), 2)

    print(o * c)


if __name__ == "__main__":
    main()