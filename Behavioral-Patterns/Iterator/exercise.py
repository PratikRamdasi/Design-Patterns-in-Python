class Node:
  def __init__(self, value, left=None, right=None):
    self.right = right
    self.left = left
    self.value = value

    self.parent = None

    if left:
      self.left.parent = self
    if right:
      self.right.parent = self

  def traverse_preorder(self):
        yield self.value
        if self.left:
            yield from self.left.traverse_preorder()
        if self.right:
            yield from self.right.traverse_preorder()
        '''
        def traverse(current):
            yield current
            if current.left:
                for left in traverse(current.left):
                    yield left
            if current.right:
                for right in traverse(current.right):
                    yield right
        
        for node in traverse(self):
            yield node.value
        '''
