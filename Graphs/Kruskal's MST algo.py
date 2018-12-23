"""     Kruskal’s Minimum Spanning Tree Algorithm 


	What is Minimum Spanning Tree?
	
	Given a connected and undirected graph, 
		a spanning tree of that graph is:
			 a subgraph that is a TREE and CONNECTS ALL the vertices together.
		
		one Graph has many spanning tree!!!
	 	

	 	A MST or minimum weight spanning tree for a weighted
	 	Connected and undirected graph is a spanning tree :
	 		weight less than or equal to the weight of every other spanning tree.
	 		The weight of a spanning tree is the sum of weights given to each edge of the spanning tree.

How many edges does a minimum spanning tree has?
 (V – 1) edges where V is the number of vertices

What are the applications of Minimum Spanning Tree?
See this for applications of MST.
Kruskal's Shortest path

**************************************************
steps for finding MST using Kruskal’s algorithm

1. Sort the edges: (non-decreasing)


2. Pick the smallest edge.
 Check if--->cycle with the spanning tree formed so far.
		If cycle is not formed:
			 include this edge
		Else:
		 	 discard it
3. Repeat step#2 until there are (V-1) edges in the spanning tree.
*****************************************************

The algorithm is a Greedy Algorithm. 
The Greedy Choice is to pick the smallest weight edge that does not cause a cycle in the MST constructed so far.





After sorting:
Weight   Src    Dest
1         7      6
2         8      2
2         6      5
4         0      1
4         2      5
6         8      6
7         2      3
7         7      8
8         0      7
8         1      2
9         3      4
10        5      4
11        1      7
14        3      5
 9 vertices (and 14 edges.)
  So, MSTformed will be having (9 – 1) = 8 edges.

"""






# Python program for Kruskal's algorithm to find 
# Minimum Spanning Tree of a given connected, 
# undirected and weighted graph 

from collections import defaultdict 

#Class to represent a graph is 
class Graph: 

	def __init__(self,vertices): 
		self.V= vertices #No. of vertices 
		self.graph = [] # default dictionary 
								# to store graph 
		

	# function to add an edge to graph 
	def addEdge(self,u,v,w): 
		self.graph.append([u,v,w]) 

	# A utility function to find set of an element i 
	# (uses path compression technique) 
	def find(self, parent, i): 
		if parent[i] == i: 
			return i 
		return self.find(parent, parent[i]) 

	# A function that does union of two sets of x and y 
	# (uses union by rank) 
	def union(self, parent, rank, x, y): 
		xroot = self.find(parent, x) 
		yroot = self.find(parent, y) 

		# Attach smaller rank tree under root of 
		# high rank tree (Union by Rank) 
		if rank[xroot] < rank[yroot]: 
			parent[xroot] = yroot 
		elif rank[xroot] > rank[yroot]: 
			parent[yroot] = xroot 

		# If ranks are same, then make one as root 
		# and increment its rank by one 
		else : 
			parent[yroot] = xroot 
			rank[xroot] += 1

	# The main function to construct MST using Kruskal's 
		# algorithm 
	def KruskalMST(self): 

		result =[] #This will store the resultant MST 

		i = 0 # An index variable, used for sorted edges 
		e = 0 # An index variable, used for result[] 

			# Step 1: Sort all the edges in non-decreasing 
				# order of their 
				# weight. If we are not allowed to change the 
				# given graph, we can create a copy of graph 
		self.graph = sorted(self.graph,key=lambda item: item[2]) 

		parent = [] ; rank = [] 

		# Create V subsets with single elements 
		for node in range(self.V): 
			parent.append(node) 
			rank.append(0) 
	
		# Number of edges to be taken is equal to V-1 
		while e < self.V -1 : 

			# Step 2: Pick the smallest edge and increment 
					# the index for next iteration 
			u,v,w = self.graph[i] 
			i = i + 1
			x = self.find(parent, u) 
			y = self.find(parent ,v) 

			# If including this edge does't cause cycle, 
						# include it in result and increment the index 
						# of result for next edge 
			if x != y: 
				e = e + 1	
				result.append([u,v,w]) 
				self.union(parent, rank, x, y)			 
			# Else discard the edge 

		# print the contents of result[] to display the built MST 
		print "Following are the edges in the constructed MST"
		for u,v,weight in result: 
			#print str(u) + " -- " + str(v) + " == " + str(weight) 
			print ("%d -- %d == %d" % (u,v,weight)) 

# Driver code 
g = Graph(4) 
g.addEdge(0, 1, 10) 
g.addEdge(0, 2, 6) 
g.addEdge(0, 3, 5) 
g.addEdge(1, 3, 15) 
g.addEdge(2, 3, 4) 

g.KruskalMST() 

#This code is contributed by Neelam Yadav 
