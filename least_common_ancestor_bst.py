# http://www.geeksforgeeks.org/lowest-common-ancestor-in-a-binary-search-tree/
from tree_utils import TreeNode


# for bst
def least_comm_ancestor(root, n1, n2):

	if not root:
		return None

	if root.data > n1 and root.data > n2:
		return least_comm_ancestor(root.left, n1, n2)

	if root.data < n1 and root.data < n2:
		return least_comm_ancestor(root.right, n1, n2)

	return root


def test():
	root = TreeNode(20)
	root.left = TreeNode(8)
	root.right = TreeNode(22)
	root.left.left = TreeNode(4)
	root.left.right = TreeNode(12)
	root.left.right.left = TreeNode(10)
	root.left.right.right = TreeNode(14)

	n1 = 10;
	n2 = 14
	t = least_comm_ancestor(root, n1, n2)
	print "LCA of %d and %d is %d" % (n1, n2, t.data)

	n1 = 14;
	n2 = 8
	t = least_comm_ancestor(root, n1, n2)
	print "LCA of %d and %d is %d" % (n1, n2, t.data)

	n1 = 10;
	n2 = 22
	t = least_comm_ancestor(root, n1, n2)
	print "LCA of %d and %d is %d" % (n1, n2, t.data)