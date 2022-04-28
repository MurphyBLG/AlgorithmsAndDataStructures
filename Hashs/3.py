def hash_f(num, m):
    sum = 0
    while num != 0:
        sum += num % 10
        num //= 10

    return sum % m


def print_table(table):
    for el in table:
        print(f"{el[0]}: {el[1]}")


def linear_search(arr, num):
    t = 0
    for el in arr:
        if el == num:
            t += 1
    
    return t


def find_num(table, num, m):
    num_hash = hash_f(num, m)
    
    print(f"Number '{num}' appears {linear_search(table[num_hash][1], num)} times in the table")


if __name__ == '__main__':
    n = int(input("Enter hash table size: "))
    hash_table = []
    for i in range(n):
        hash_table.append([i, []])

    with open("input2.txt", "r") as f:
        for line in f.readlines():
            for word in line.split():
                hash_table[hash_f(int(word), n)][1].append(int(word))

    print_table(hash_table)

    number = int(input("Enter number you're searching: "))
    find_num(hash_table, number, n)
