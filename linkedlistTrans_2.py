''' welcome to transversal of linked list 

TRANSVERSAL AND PRINTING 
--- for this purpose lets add  a function 
    in linked list to print entire list ''' 

#node

class Node:
	''' has two things: data  next'''
	def __init__(self,data):
		self.data  = data
		self.next  = None

#ll

class Linkedlist:
	''' has a head node  '''
	def __init__(self):
		self.head = None #initially head is null

	def print(self):
		temp = self.head
		g=""
		while temp:
			g+=str(temp.data) +"-->"
			temp = temp.next
		print(g)

	









ll = Linkedlist()
ll.head = Node("sameer")
second = Node("code")
third = Node("google")

ll.head.next = second
second.next = third

ll.print()

ll.print()