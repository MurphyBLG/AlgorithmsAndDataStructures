from datetime import datetime
import time


def merge (left_part: list, right_part: list) -> list:
    merged_list = []

    i = 0
    j = 0
    while i < len(left_part) and j < len(right_part):
        if left_part[i] < right_part[j]:
            merged_list.append(left_part[i])
            i+=1
        else:
            merged_list.append(right_part[j])
            j+=1

    while i < len(left_part):
        merged_list.append(left_part[i])
        i+=1

    while j < len(right_part):
        merged_list.append(right_part[j])
        j+=1
    
    return merged_list



def merge_sort(arr: list) -> list:
    if len(arr) > 1:
        left_part = merge_sort(arr[:len(arr)//2])
        right_part = merge_sort(arr[len(arr)//2:])

        return merge(left_part, right_part)
    else:
        return arr




if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))

    start_time = datetime.now()

    arr = merge_sort(arr)
    ans = 0
    for i in range(len(arr)//2, len(arr)):
        ans += arr[i]

    print(f'{ans}\n time: {datetime.now() - start_time}')
    