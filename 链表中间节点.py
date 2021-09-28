class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middleNode(head: ListNode):
    count = 1
    node = head
    while node.next:
        count += 1
        node = node.next
    mid_idx = count // 2 + 1
    node = head
    for i in range(1, mid_idx):
        node = node.next
    return node


if __name__ == "__main__":
    tail = ListNode(5)
    node3 = ListNode(4, tail)
    node2 = ListNode(3, node3)
    node1 = ListNode(2, node2)
    head = ListNode(1, node1)
    middleNode(head)
