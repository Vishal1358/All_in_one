class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class AndBinaryTree:
    def __init__(self, depth):
        self.root = self._build_tree(depth)

    def _build_tree(self, depth):
        if depth == 0:
            return None
        else:
            left = self._build_tree(depth-1)
            right = self._build_tree(depth-1)
            return Node(1, left, right)

    def update(self, path, value):
        node = self.root
        for bit in path:
            if bit == 0:
                node = node.left
            else:
                node = node.right
        node.value = value
        self._propagate_update(node)

    def _propagate_update(self, node):
        if node.left is None and node.right is None:
            return
        if node.left.value == 0 or node.right.value == 0:
            node.value = 0
        else:
            node.value = 1
        self._propagate_update(node.left)
        self._propagate_update(node.right)

    def print_tree(self):
        self._print_tree(self.root)

    def _print_tree(self, node, level=1):
        if node is not None:
            self._print_tree(node.left, level+1)
            print('L{} {}'.format(level, ' '.join(str(node.value) for _ in range(level))))
            self._print_tree(node.right, level+1)

tree = AndBinaryTree(depth=6)
tree.print_tree()

# Update the third leaf node at level 1 to 0
tree.update([0, 1, 0, 0, 1], 0)
tree.print_tree()
