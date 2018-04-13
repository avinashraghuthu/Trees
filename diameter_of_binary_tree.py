#  http://www.geeksforgeeks.org/diameter-of-a-binary-tree-in-on-a-new-method/

from tree_utils import TreeNode


def diameter_util(root):
	if not root:
		return 0

	left_height = diameter_util(root.left)
	right_height = diameter_util(root.right)

	diameter_util.res = max(diameter_util.res, left_height + 1 + right_height)

	return 1 + max(left_height, right_height)


def diameter(root):
	diameter_util.res = float('-inf')
	diameter_util(root)
	return diameter_util.res


def test():
	root = TreeNode(1)
	root.left = TreeNode(2)
	root.right = TreeNode(3)
	root.left.left = TreeNode(4)
	root.left.right = TreeNode(5)
	print "Diameter: " + str(diameter(root))
