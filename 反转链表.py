class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print(self):
        print(self.val)
        node = self
        while node.next:
            print(node.next.val)
            node = node.next


def reverseList(head:ListNode) -> ListNode:
    node = head
    stack = [node]
    while node.next:
        stack.append(node.next)
        node = node.next
    node = stack.pop()
    head = node
    while stack:
        node.next = stack.pop()
        node = node.next
    node.next = None
    return head


if __name__ == "__main__":
    tail = ListNode(4)
    node3 = ListNode(3, next=tail)
    node2 = ListNode(2, next=node3)
    node1 = ListNode(1, next=node2)
    head = ListNode(0, next=node1)
    head.print()
    ans = reverseList(head=head)
    ans.print()
