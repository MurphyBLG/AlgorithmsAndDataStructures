from datetime import datetime
import time


def count_sort(arr: list) -> list:
    min_el = min(arr)
    max_el = max(arr)

    if min_el < 0:
        for el in arr:
            el += -min_el
        
        max_el += -min_el
        min_el = 0

    cnt = [0 for _ in range(max_el + 1)]
    for el in arr:
        cnt[el] += 1

    for i in range(1, len(cnt)):
        cnt[i] += cnt[i - 1]

    ans = arr.copy()
    for el in arr:
        ans[cnt[el] - 1] = el
        cnt[el]-=1

    return ans


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))

    start_time = datetime.now()

    arr = count_sort(arr)
    ans = 0
    for i in range(len(arr)//2, len(arr)):
        ans += arr[i]

    print(f'{ans}\n time: {datetime.now() - start_time}')