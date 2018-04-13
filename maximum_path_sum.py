#  http://www.geeksforgeeks.org/find-maximum-path-sum-in-a-binary-tree/
from tree_utils import TreeNode

# Python program to find maximum path sum in Binary Tree


def find_max_sum_util(root):

	if not root:
		return 0

	l_val = find_max_sum_util(root.left)
	r_val = find_max_sum_util(root.right)

	max_single = max(max(l_val,r_val)+ root.data, root.data)

	max_top = max(max_single, l_val + root.data + r_val)

	find_max_sum_util.res = max(find_max_sum_util.res, max_top)

	return max_single


def find_max_sum(root):

	find_max_sum_util.res = float('-inf')

	find_max_sum_util(root)

	return find_max_sum_util.res


def test():
	root = TreeNode(10)
	root.left = TreeNode(2)
	root.right = TreeNode(10)
	root.left.left = TreeNode(20)
	root.left.right = TreeNode(1)
	root.right.right = TreeNode(-25)
	root.right.right.left = TreeNode(3)
	root.right.right.right = TreeNode(4)
	print "Max path sum is ", find_max_sum(root)