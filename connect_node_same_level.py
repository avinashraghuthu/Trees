#  http://www.geeksforgeeks.org/connect-nodes-level-level-order-traversal/


class Node(object):

	def __init__(self, data):
		self.data = data
		self.left = self.right = self.next_right = None


def connect_nodes(root):
	level_queue = []
	level_queue.append(root)
	level_queue.append(None)
	while level_queue:
		node = level_queue.pop(0)
		if node:
			node.next_right = level_queue[0]
			if node.left:
				level_queue.append(node.left)
			if node.right:
				level_queue.append(node.right)
		elif level_queue:
			level_queue.append(None)

def test():
	root = Node(10)
	root.left = Node(8)
	root.right = Node(2)
	root.left.left = Node(3)
	root.right.right = Node(90)
	connect_nodes(root)
	print root.next_right.data if root.next_right else -1
	print root.left.next_right.data if root.left.next_right else -1
	print root.right.next_right.data if root.right.next_right else -1
	print root.left.left.next_right.data if root.left.left.next_right else -1
	print root.right.right.next_right.data if root.right.right.next_right else -1