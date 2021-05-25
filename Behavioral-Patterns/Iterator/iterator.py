# iterate a binary tree
class Node:
    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value

        self.parent = None # parent of the current node

        if left: # child on left side
            self.left.parent = self
        if right: # child on right side
            self.right.parent = self

# ietartor has states -> needs to know current element to go to next
class InOrderIterator:
    def __init__(self, root):
        self.root = self.current = root
        self.yielded_start = True

        while(self.current.left):
            self.current = self.current.left 

### CHECK tree_trasversal.py

if __name__ == "__main__":
    #   1
    #  / \
    # 2   3
    # inorder - 213
    root = Node(1, Node(2), Node(3))

    # iterate from root

        