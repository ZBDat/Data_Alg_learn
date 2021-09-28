class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.lchild = left
        self.rchild = right


class Tree:
    def __init__(self):
        self.root = Node()
        self.queue = []  # 保存的是未满子树

    def add(self, val: int):
        node = Node(val)
        if self.root.val is None:
            self.root = node
            self.queue.append(self.root)
        else:
            treeNode = self.queue[0]
            if treeNode.lchild is None:
                treeNode.lchild = node
                self.queue.append(treeNode.lchild)
            else:
                treeNode.rchild = node
                self.queue.append(treeNode.rchild)
                self.queue.pop(0)  # 填充完右孩子之后父节点已经满，弹出

    #  递归版本的遍历，摆正顺序便可
    def preorder_recursion(self, root):
        if not root:
            return
        print(root.val)
        self.preorder_recursion(root.lchild)
        self.preorder_recursion(root.rchild)

    def inorder_recursion(self, root):
        if not root:
            return
        self.inorder_recursion(root.lchild)
        print(root.val)
        self.inorder_recursion(root.rchild)

    def postorder_recursion(self, root):
        if not root:
            return
        self.postorder_recursion(root.lchild)
        self.postorder_recursion(root.rchild)
        print(root.val)


if __name__ == "__main__":
    vals = range(10)
    tree = Tree()
    for val in vals:
        tree.add(val)
