#  http://www.geeksforgeeks.org/symmetric-tree-tree-which-is-mirror-image-of-itself/

from tree_utils import TreeNode


def is_mirror(root1, root2):
	if not root1 and not root2:
		return True

	if root1 and root2:
		return (root1.data == root2.data) and \
				is_mirror(root1.left, root2.right) and \
				is_mirror(root1.right, root2.left)
	return False


def is_symmetric(root):
	return is_mirror(root, root)


def test():
	root = TreeNode(1)
	root.left = TreeNode(2)
	root.right = TreeNode(2)
	root.left.left = TreeNode(3)
	root.left.right = TreeNode(4)
	root.right.left = TreeNode(4)
	root.right.right = TreeNode(3)
	print is_symmetric(root)
