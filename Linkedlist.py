''' linked list has 
        Node --
                DATA
                pointer to next node

        head-- 
                first node
'''

class Node:

    #initialiseze the node object
    def __init__(self,data):
        self.data = data #assign data
        self.next = None #initialize next as null

# lets make a lined list class made of nodes

class Linkedlist:

    #function to initialise head points to next node


    def __init__(self):
        self.head = None

'''start empty list'''
ll = Linkedlist()

ll.head = Node(1)
second  = Node(2)
third = Node(3)

''' node 1 is a special node as its got a head

'''
ll.head = second
second.next = third


'''
llist.head        second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  |  o-------->| 2  |  o-------->|  3 | null |
    +----+------+     +----+------+     +----+------+ 
    


    '''







