class Node:
    def __init__(self, num = None):
        self.data = num
        self.next = None
        self.prev = None


class Linked_list:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.sum = 0
        self.count = 0


    def push_back(self, num):
        new_node = Node(num)
        self.sum += num
        self.count += 1
    
        if self.head == None:
            self.head = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node

        self.tail = new_node       


    def get_avg(self):
        return self.sum // self.count


    def change(self):
        self.head.data = self.get_avg()     
        
    
    def print_list(self):
        tmp = self.head

        while tmp:
            print(f'{tmp.data} ', end="")
            tmp = tmp.next
        


if __name__ == '__main__':

    List = Linked_list()

    n = int(input())
    while n != 0:
        x = int(input())
        List.push_back(x)
        n -= 1

    List.change()
    List.print_list()

    








    

