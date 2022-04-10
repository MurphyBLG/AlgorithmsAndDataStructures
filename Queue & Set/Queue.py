if __name__ == "__main__":
    n = int(input())

    queue = []
    minimum = None
    first_el = None
    for i in range(n):
        queue.append(int(input()))
        if len(queue) == 1:
            first_el = minimum = queue[0]
        else:
            minimum = min(minimum, queue[-1])
    
    new_queue = []
    new_queue.append(minimum)
    queue.pop(0)
    flag = False
    while len(queue) > 0:
        tmp = queue.pop(0)
        if tmp == minimum and not flag:
            new_queue.append(first_el)
            flag = True
        else:
            new_queue.append(tmp)

    while len(new_queue) > 0:
        print(new_queue.pop(0))

        
