''' trees are hierarchical data_structure 
    topmost node = root
element directly under it__ called its children
above it --- parent

elements with no children are called root


why use tree ?
	to store info that follow hierachy
	file sys on a computer
whats a binary tree?
	an element has at the most two children.
	left and right child.
how is tree represented ?
	represented by node at the top
	if node is empty then tree is empty!!


A tree node :
	has data 
	pointer to right node 
	pointer to left node
'''
 
 class Node(object):
 	def __init__(self,data):
	 	self.data = data
	 	self.right = right
	 	self.left = left

	 root = Node("life")
	 root.left = Node("good")
	 root.right = Node("bad")
	 root.left.left = Node("money")
	 root.left.right = Node("love")
	 root.right.left = Node("poor")
	 root.right.right = Node("sad!")
