from count_sort_variant import count_sort
from merge_sort_variant import merge_sort
from datetime import datetime
import time

n = int(input("Enter count of elements: "))

ms = [n - i for i in range(n)]
cs = [n - i for i in range(n)]

descending_ms_time = datetime.now()
ms = merge_sort(ms)
descending_ms_time = datetime.now() - descending_ms_time
 

descending_cs_time = datetime.now()
cs = count_sort(cs)
descending_cs_time = datetime.now() - descending_cs_time

ms.clear() 
cs.clear()
for i in range(n):
    if (i < n // 2):
        ms.append(i)
        cs.append(i)
    else:
        ms.append(n - i)
        cs.append(n - i)

half_descending_ms_time = datetime.now()
ms = merge_sort(ms)
half_descending_ms_time = datetime.now() - half_descending_ms_time
 

half_descending_cs_time = datetime.now()
cs = count_sort(cs)
half_descending_cs_time = datetime.now() - half_descending_cs_time


print("descending: ")
print(f" ms: {descending_ms_time}")
print(f" cs: {descending_cs_time}")

print("half descending: ")
print(f" ms: {half_descending_ms_time}")
print(f" cs: {half_descending_cs_time}")
