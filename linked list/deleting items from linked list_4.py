'''
To delete a node from linked list, we need to do following steps.
1) Find previous node of the node to be deleted.
2) Changed next of previous node.
3) Free memory for the node to be deleted.





delete a node'''

#node
class Node:

	def __init__(self,data):
		self.data = data
		self.next = None

#linked list
class Linked:

	def __init__(self):
		self.head = None

	def delete(self,key):
		#store head node
		temp = self.head

		#if head is the key 
		if temp.data ==key:
			slef.head = temp.next
			temp = None
			return
		# Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'

        while (temp is not None):
        	if temp.data == key:
        		break
        	prev = temp
        	temp  = temp.next
        	#we dont want prev ka next 
        	# so prev. next ko delete wale next ke agey asign

        if(temp == None):
        	return
        #didnt find the key
        #unlink the node
        prev.next = temp.next

        #lets free the  memory
        temp = None 

    def del_pos(self,pos):
    	#check if its empty

    	if self.head is None:
    		return
    	
    	#check if its zeroth element 

    	if pos ==0:
    		self.head = None
    		return

    	#iterate till the prev element 
    	
    	#store head
    	temp = self.head
    	for i in range(pos -1):
    		temp  = temp.next
    		if temp is None:
    			return
    	# temp is Previous:
    	
    	#if the item doesnt exist return

    	if temp.next is None:
    		return

    	#lets delink it now
''' join the previous node to next to next node: '''
		t = temp.next.next

		#free the data
		temp.next = None
		temp.next = t 









