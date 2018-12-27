'''Trees are non-linear data structure
they can be transversed in many ways:

   
   
   A.Depth first Traversal
        1.Inorder(left root right)
        2. Preorder(root left right )
        3. Postorder(left right root)
    
    B. Breadth first Traversal:
        
        
    
        
        


'''
class Node:
	def __init__(self,data):
			self.data = data 
			self.left = None
			self.right = None

def inorder(root):
	if root is not None:
		inorder(root.left)
		print(root.data)
		inorder(root.right)

def postorder(root):
	if root is not None:
		postorder(root.left)
		postorder(root.right)
		print(root.data)

def preorder(root):
	if root is not None:
		print(root.data)
		preorder(root.left)
		preorder(root.right)



root=Node(1)
a=Node(2)
b=Node(3)
c=Node(4)
d=Node(5)
root.left=a
root.right=b
a.left=c
a.right=d
print("pre")
preorder(root)
print("post")
postorder(root)
print("inorder")
inorder(root)
