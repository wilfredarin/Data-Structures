''' 
	1.front -- push
	2.after a given node -- insertAfter
	3. at end -- append


'''
'''
 ---at first : 4 step process ---
 node added before head
 new node becomes the head 
 ********** push() *********
 push needs the header pointer
 '''
class Node:
 	def __init__(self,data):
 		self.data = data
 		self.next = None


class Linkedlist:
	def __init__(self):
 		self.head = None
 	

	def print(self):
 		temp=self.head
 		g = ""
 		while temp:
 			g+=str(temp.data)+"-->"
 			temp = temp.next
 		print(g)
 	
	def push(self,new_data):
 		#make the data a node
 		new_data = Node(new_data)

 		new_data.next = self.head

 		self.head = new_data

# to add after a given node  5 steps
	

	def insertAfter(self,given_node,new_data):
		#check if the give node exists:
		if given_node is None:
			print("please enter a valid node**!**")
			return

		#lets make the new_data a node:

		new_node = Node(new_data)

		#so the given nodes next node has to the new node
		

		# and new_node ka next would be the next of given_node

		new_node.next = given_node.next
		given_node.next = new_node



	''' adding a  node at the end  6 steps'''

	def append(self,new_data):

		#lets create a new_node:
		new_node = Node(new_data)
		#lets set its next as none as its the last one
		new_node.next = None
		
		#if linkl is empty :
		#then this would be our head
		if self.head is None:
			self.head = new_node
			return
		#else traverse till the last node
		last = self.head
		
		while (last.next):
			last = last.next

		#change the next of the last

		last.next = new_node
	

ll = Linkedlist()
ll.append("sameer ranjan")
ll.push("hello world")
ll.insertAfter(ll.head.next,"ends")

ll.print()
