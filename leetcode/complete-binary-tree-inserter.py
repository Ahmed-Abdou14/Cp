# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):

        pointer = root
        height = 0
        while pointer:
            height += 1
            pointer = pointer.left

        self.arr = [None] * (2 ** height - 1)
        self.arr[0] = root

        def loop_by_level(root: TreeNode, i: int = 0):
            if root.left:
                index = i*2 + 1
                self.arr[index] = root.left
                loop_by_level(root.left, index)
            if root.right:
                index = i*2 + 2
                self.arr[index] = root.right
                loop_by_level(root.right, index)

        loop_by_level(root, 0)
        self.arr = list(filter(lambda x: x, self.arr))

    def insert(self, val: int) -> int:
        new_node = TreeNode(val)

        parent = self.arr[(len(self.arr) - 1) // 2]

        if not parent.left:
            parent.left = new_node
        else:
            parent.right = new_node

        self.arr.append(new_node)
        return parent.val

    def get_root(self) -> Optional[TreeNode]:
        return self.arr[0]
