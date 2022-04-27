def print_table(table):
    for el in table:
        print(f"{el[0]}: {el[1]}")


def roflan_hashfun(char):
    return ord(char) - 97


if __name__ == "__main__":
    sent = input("Enter string: ").lower()

    hash_table = []
    for i in range(26):
        hash_table.append([chr(97+i), 0])
    
    for c in sent:
        if c.isalpha():
            hash_table[roflan_hashfun(c)][1] += 1

    
    letter = input("Enter letter you're searching: ")
    letter_hash = roflan_hashfun(letter)
    if hash_table[letter_hash][1] != 0:
        print(f'Hash table cotains letter "{letter}"\nCount of letter "{letter}" is {hash_table[letter_hash][1]}')
    else:
        print(f'There is no letter "{letter}"')