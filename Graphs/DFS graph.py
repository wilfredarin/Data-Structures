""" Depth First Search or DFS for a Graph
similar to Depth First Traversal of a tree.
unlike trees, GRAPH CONTAINS CYCLE!, so we may come to the same node again. 
    use a boolean visited array.


(0,2)(2,0)(1,2)(2,3)(3,3) start:->2

 ---->2, 0, 1, 3
"""

# Python program to print DFS traversal from a 
# given given graph 

from collections import defaultdict 

# This class represents a directed graph using 
# adjacency list representation 
class Graph: 

	# Constructor 
	def __init__(self): 

		#graph is a dictionary containig 
		# default dictionary to store graph 
		self.graph = defaultdict(list) 

	#function to add an edge to graph 
	#so this edge uses a adjacency list implementation

	def addEdge(self,u,v): 
		self.graph[u].append(v) 

	# A function used by DFS 
	def DFSUtil(self,v,visited): 

		# Mark the current node as visited and print it 
		visited[v]= True
		print(v) 

		# Recur for all the vertices adjacent to this vertex 
		for i in self.graph[v]: 
			if visited[i] == False: 
				self.DFSUtil(i, visited) 


	# The function to do DFS traversal. It uses 
	# recursive DFSUtil() 
	def DFS(self,v): 

		# Mark all the vertices as not visited 
		visited = [False]*(len(self.graph)) 

		# Call the recursive helper function to print 
		# DFS traversal 
		self.DFSUtil(v,visited) 


# Driver code 
# Create a graph given in the above diagram 
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 

print ("Following is DFS from (starting from vertex 2)")
g.DFS(2) 

# This code is contributed by Neelam Yadav 
