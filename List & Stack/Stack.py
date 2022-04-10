
from operator import truediv
from xmlrpc.client import MAXINT


if __name__ == "__main__":
    n = int(input())

    stack = []
    avg = 0.0
    for i in range(n):
        stack.append(float(input()))
        avg += stack[-1]

    avg /= n

    tmp = []
    num = stack.pop()
    tmp.append(num)
    dist = abs(avg - num)
    while len(stack) > 0:
        tmp.append(stack.pop())
        if abs(avg - tmp[-1]) < dist:
            dist = abs(tmp[-1] - avg)
            num = tmp[-1]

    flag = False
    while len(tmp) > 0:
        a = tmp.pop()
        if a == num and not flag:
            flag = True
            continue
        else:
            stack.append(a)
    stack.append(num)

    while len(stack) > 0:
        print(stack.pop())
        

