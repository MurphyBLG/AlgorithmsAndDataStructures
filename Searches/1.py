from re import U


def lower_bound(value: int, arr: list) -> int:
    L = -1
    R = len(arr) - 1

    while R - L > 1:
        M = (R + L) // 2
        if arr[M] >= value:
            R = M
        else:
            L = M
    
    if arr[R] == value:
        return R
    else:
        return -1
    

def upper_bound(value: int, arr: list) -> int:
    L = 0
    R = len(arr)

    while R - L > 1:
        M = (R + L) // 2
        if arr[M] <= value:
            L = M
        else:
            R = M
    
    if arr[L] == value:
        return L
    else:
        return -1
    

if __name__ == '__main__':
    n = int(input())
    key = int(input())
    arr = list(map(int, input().split()))

    arr.sort()
    
    lower_bound = lower_bound(key, arr)
    upper_bound = upper_bound(key, arr)

    if lower_bound == -1 and upper_bound == -1:
        print(f'There is no "{key}" in array')
    elif lower_bound == -1 and upper_bound != -1:
        print(f'There are {upper_bound + 1} elements with value "{key}"\n' 
        + f'Starts with 0 and ends with {upper_bound}')
    elif lower_bound != -1 and upper_bound == -1:
        print(f'There are {n - lower_bound} elements with value "{key}"\n' 
        + f'Starts with {lower_bound} and ends with {n - 1}')
    else:
        print(f'There are {upper_bound - lower_bound + 1} elements with value "{key}"\n' 
        + f'Starts with {lower_bound} and ends with {upper_bound}')

