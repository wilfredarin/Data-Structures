''' 
queue : jsut like  Consumer queue
FIFO

enqueue: add to queue 

Dequeue : Remove an item to the queue

insertion and deletion happens on different
endslast item from que

front : get the front item from queue
rear : Get the last item from the queue



used when things dont have to be processed immediately


its like breadth search

For implementing queue,
 we need to keep 
track of two indices, front and rear.

    ARRAY implementation of Queue
    

class Queue  has four things :
	capacity 
	front
	end 
	Q
'''

class Queue(object):
	"""this has 4 things :                               """
	def __init__(self,capacity):
		self.front = self.size = 0 # its a number 
		self.rear = capacity-1  #gets the last item from the queue :.... its a number 
		self.Q = [None]*capacity  
		self.capacity  = capacity

	#when size of the Queue is equal to the capacity :> its full!!!
	
	def isFull(self):
		return self.size == self.capacity
	#empty when size is 0
	def isEmpty(self):
		return self.size == 0

	#adding item changes rear last item & size

	def EnQueue(self,data):
		"""check if its full """
		if self.isFull():
			return (print("The Queue is full !"))

		self.rear  = (self.rear + 1) % self.capacity
		#lets add the item to the list  at the end
		self.Q[self.rear] = data

		# updating the size of the array

		self.size +=1
		print("item ",data,"EnQueued to the Queue")

	# removing the data Dequeue changes: Front and the size

	def DeQueue(self):
		''' check if its empty ''' 
		if self.isEmpty():
			print("Empty!")
			return

		print("item #",self.Q[front],"# has been succesfully removed.")

		#so now front has to be increased as the item on  0 ("sam")  1("rat") 2("cat") 3("mat")
		#becomes   now no more sam so now in front 1("rat")   
		#front changes from 0 ------> 1
		#what if keep removing --- front increases -- reaches capacity-1 now what ????

		# ok but then size will become zero and an empty Queue would be flaged
		# now lets add an item in the Queue so front += 1   out of the Queue ? index out of range 
		# solution is this 

		self.front = (self.front + 1)% self.capacity
		self.size -= 1

	def q_front(self):
		if self.isEmpty():
			print("sir i am empty")
			return
		print(self.Q[self.front])
		return
	def q_rear(self):
		if self.isEmpty():
			print("sir i am empty")
			return
		print(self.Q[self.rear])
		return 


q1= Queue(4)

q1.EnQueue("sameer")
print(q1.q_front())




















