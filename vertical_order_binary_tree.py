from tree_utils import TreeNode


def get_horizontal_distance_map(root, horizontal_distance, horizontal_distance_map):
	if not root:
		return

	try:
		horizontal_distance_map[horizontal_distance].append(root.data)
	except Exception, e:
		horizontal_distance_map[horizontal_distance] = [root.data]

	get_horizontal_distance_map(root.left, horizontal_distance-1, horizontal_distance_map)
	get_horizontal_distance_map(root.right, horizontal_distance+1, horizontal_distance_map)


def display_vertical_order(root):

	horizontal_distance_map = dict()
	horizontal_distance = 0
	get_horizontal_distance_map(root, horizontal_distance, horizontal_distance_map)

	sorted_hd_list = sorted(horizontal_distance_map)
	for hd in sorted_hd_list:
		for i in horizontal_distance_map[hd]:
			print i,
		print


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
	print "Vertical order traversal is"
	display_vertical_order(root)