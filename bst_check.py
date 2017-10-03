from tree_utils import *
from sys import maxint


def is_bst(root):
	min_int = -maxint -1
	return is_bst_util(root, min_int, maxint)


def is_bst_util(root, min_val, max_val):
	if not root:
		return True

	if root.data < min_val or root.data > max_val:
		return False

	return is_bst_util(root.left, min_val, root.data) and \
		   is_bst_util(root.right, root.data, max_val)


# Driver program to test above function
def test():
	# root = TreeNode(3)
	# root.left = TreeNode(2)
	# root.right = TreeNode(5)
	# root.left.left = TreeNode(1)
	# root.left.right = TreeNode(4)

	l1 = TreeNode(4, None, None)
	l2 = TreeNode(5, None, None)
	l3 = TreeNode(6, None, None)
	l4 = TreeNode(7, None, None)
	l11 = TreeNode(2, l1, l2)
	l21 = TreeNode(3, l3, l4)
	root = TreeNode(1, l11, l21)
	if is_bst(root):
		print "Is BST"
	else:
		print "Not a BST"