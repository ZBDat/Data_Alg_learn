class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        # loop list, do not need a tail.
        self.head = None

    @property
    def is_empty(self):
        return not self.head

    def length(self):
        if self.is_empty:
            return 0
        else:
            cur = self.head.next
            n = 1
            while cur != self.head:
                cur = cur.next
                n += 1
            return n

    def add(self, data):
        # add element in at the beginning
        node = Node(data)
        if self.is_empty:
            node.next = node
            node.prev = node
            self.head = node
        else:
            node.next = self.head
            node.prev = self.head.prev
            self.head.prev.next = node
            self.head.prev = node
            self.head = node

    def append(self, data):
        # add element at the end
        if self.is_empty:
            self.add(data)
        else:
            node = Node(data)
            node.next = self.head
            node.prev = self.head.prev
            self.head.prev.next = node
            self.head.prev = node

    def printlist(self):
        if self.is_empty:
            print("the list is empty!")

        else:
            print(self.head.data)
            cur = self.head.next
            while cur != self.head:
                print(cur.data)
                cur = cur.next


if __name__ == "__main__":
    l = LinkedList()
    print(l.is_empty)
    l.add(1)
    l.add(0)
    l.add(0)
    l.append(2)
    l.append(3)
    print(l.length())
    l.printlist()