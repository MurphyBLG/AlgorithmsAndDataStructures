def hash_fun(word, m):
    return (ord(word[0]) - 97) % m


def print_table(table):
    for el in table:
        print(f"{el[0]}: {el[1]}")


def linear_search(arr, word):
    t = 0
    for el in arr:
        if el == word:
            t += 1
    
    return t


def find_word(table, word, m):
    word_hash = hash_fun(word, m)
    
    print(f"Word '{word}' appears {linear_search(table[word_hash][1], word)} times in the table")


def delete(table, letter, m):
    letter_hash = hash_fun(letter, m)

    tmp = []
    for el in table[letter_hash][1]:
        if el[0] != letter:
            tmp.append(el)

    table[letter_hash][1] = tmp



if __name__ == "__main__":
    n = int(input("Enter hash table size: "))
    hash_table = []
    for i in range(n):
        hash_table.append([i, []])

    with open("input.txt", "r") as f:
        for line in f.readlines():
            for word in line.split():
                hash_table[hash_fun(word.lower(), n)][1].append(word.lower())

    print_table(hash_table)

    word = input("Enter word you're searching: ")
    find_word(hash_table, word, n)
    
    letter = input("Enter letter: ")
    delete(hash_table, letter, n)

    print_table(table=hash_table)
