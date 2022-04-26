def calc_shifts(word):
    shift = {}
    for i in range(len(word) - 2, -1, -1):
        if word[i] not in shift.keys():
            shift[word[i]] = len(word) - i

    if word[len(word) - 1] not in shift.keys():
        shift[word[len(word) - 1]] = len(word)

    shift['*'] = len(word)
    
    return shift


def find(word, text):
    i = len(word) - 1

    while i < len(text):
        k = 0

        while text[i - k] == word[len(word) - k - 1] and k != len(word):
            k += 1

        if k == len(word):
            print(i - k + 1)
            i += k
        else:
            if k == 0:
                i += min(len(text) - i, shifts[word[len(word) - 1]])
            else:
                i += min(len(text) - i + k, shifts[word[len(word) - k - 1]])



if __name__ == '__main__':
    word = input("Enter substr: ")
    shifts = calc_shifts(word)

    with open("input.txt", "r") as f:
        text = f.read()
    
    print("Indexes: ")
    find(word, text)
