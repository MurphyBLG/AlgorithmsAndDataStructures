if __name__ == '__main__':
    hash_table = {}
    with open("input.txt", "r") as f:
        for line in f.readlines():
            for word in line.split():
                if word in hash_table:
                    hash_table[int(word)] += 1
                else:
                    hash_table[int(word)] = 1

    num = int(input())
    if num in hash_table.keys():
        print(f'Hash table cotains num "{num}"\nCount of num "{num}" is {hash_table[num]}')
    else:
        print(f'There is no num "{num}"')
