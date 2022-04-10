from pprint import pprint

if __name__ == "__main__":
    hash_table = {}
    sent = input().lower()


    for c in sent:
        if c.isalpha():
            if c in hash_table.keys():
                hash_table[c] += 1
            else:
                hash_table[c] = 1

    pprint(hash_table)
    
    letter = input()
    if letter in hash_table.keys():
        print(f'Hash table cotains letter "{letter}"\nCount of letter "{letter}" is {hash_table[letter]}')
    else:
        print(f'There is no letter "{letter}"')