from pprint import pprint

if __name__ == "__main__":
    hash_table = {}

    with open("input.txt", "r") as f:
        for line in f.readlines():
            for word in line.split():
                if word in hash_table:
                    hash_table[word] += 1
                else:
                    hash_table[word] = 1

    pprint(hash_table)

    word = input()
    if word in hash_table.keys():
        print(f'Hash table cotains word "{word}"\nCount of word "{word}" is {hash_table[word]}')
    else:
        print(f'There is no word "{word}"')

    letter = input()
    tmp_dict = hash_table.copy()
    for itm in tmp_dict.keys():
        if itm.startswith(letter):
            del hash_table[itm]
    
    print(hash_table)
