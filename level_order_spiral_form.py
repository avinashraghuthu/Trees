# http://www.geeksforgeeks.org/level-order-traversal-in-spiral-form/
from tree_utils import TreeNode


def print_level_order_spiral(root):

	if not root:
		return

	s1 = list()  # To print from right to left
	s2 = list()  # To print from left to right
	s1.append(root)
	while len(s1) != 0 or len(s2) != 0:
		while len(s1) != 0:
			node = s1.pop()
			print node.data,
			if node.right:
				s2.append(node.right)
			if node.left:
				s2.append(node.left)
		while len(s2) != 0:
			node = s2.pop()
			print node.data,
			if node.left:
				s1.append(node.left)
			if node.right:
				s1.append(node.right)


def test():
	root = TreeNode(1)
	root.left = TreeNode(2)
	root.right = TreeNode(3)
	root.left.left = TreeNode(4)
	root.left.right = TreeNode(5)
	root.right.left = TreeNode(6)
	root.right.right = TreeNode(7)
	root.right.left.right = TreeNode(8)
	root.right.right.right = TreeNode(9)
	print_level_order_spiral(root)