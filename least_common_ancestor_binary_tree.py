# http://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/
from tree_utils import TreeNode

# Method 1: By finding path


def find_path(root, path, element):

	if not root:
		return False

	path.append(root.data)

	if root.data == element:
		return True

	if (root.left and find_path(root.left, path, element)) or \
			(root.right and find_path(root.right, path, element)):
		return True

	path.pop()

	return False


def lca_by_path(root, n1, n2):
	n1_path = []
	n2_path = []
	n1_exist = find_path(root, n1_path, n1)
	n2_exist = find_path(root, n2_path, n2)
	if not n1_exist or not n2_exist:
		return -1

	i=0
	while i < len(n1_path) and i < len(n2_path):
		if n1_path[i] != n2_path[i]:
			break
		i += 1
	return n1_path[i-1]


# Method 2
def lca_by_single_traversal(root, n1, n2):
	if not root:
		return None

	if root.data == n1 or root.data == n2:
		return root

	left_lca = lca_by_single_traversal(root.left, n1 , n2)
	right_lca = lca_by_single_traversal(root.right, n1, n2)

	if left_lca and right_lca:
		return root

	return left_lca if left_lca else right_lca


def test_method1():
	root = TreeNode(1)
	root.left = TreeNode(2)
	root.right = TreeNode(3)
	root.left.left = TreeNode(4)
	root.left.right = TreeNode(5)
	root.right.left = TreeNode(6)
	root.right.right = TreeNode(7)

	# print "LCA(4, 5) = %d" % (lca_by_path(root, 4, 5))
	# print "LCA(4, 6) = %d" % (lca_by_path(root, 4, 6))
	# print "LCA(3, 4) = %d" % (lca_by_path(root, 3, 4))
	# print "LCA(2, 4) = %d" % (lca_by_path(root, 2, 4))

	print "LCA(4, 5) = %d" % (lca_by_single_traversal(root, 4, 5).data)
	print "LCA(4, 6) = %d" % (lca_by_single_traversal(root, 4, 6).data)
	print "LCA(3, 4) = %d" % (lca_by_single_traversal(root, 3, 4).data)
	print "LCA(2, 4) = %d" % (lca_by_single_traversal(root, 2, 4).data)
