""" Depth First Search or DFS for a Graph
similar to Depth First Traversal of a tree.
unlike trees, GRAPH CONTAINS CYCLE!, so we may come to the same node again. 
    use a boolean visited array.


(0,2)(2,0)(1,2)(2,3)(3,3) start:->2

 ---->2, 0, 1, 3
"""





from collections import defaultdict

#what does default dict do?
#it simply initialise a dicionary
#with default for ex: list item(defaultdict(list))
#more on default dict 
#https://docs.python.org/3/library/collections.html#collections.defaultdict


class Graph:

    #constructor
    def __init__(self):
    #graph is a dictionary containig 
    # default list to store graph
        self.graph = defaultdict(list)
    #function to add an edge to graph 
    #so this edge uses a adjacency list implementation
    
    def addEdge(self,src,dst):
        self.graph[src].append(dst)

    #a function used by DFS
    def dfsUtil(self,v,visited):
        #visited is a list of visited nodes
        # Mark the current node as visited and print it 
        visited[v]= True
        #it could have performed any procedure other than printing also
        print(v) 

        # Recur for all the vertices adjacent to this vertex 
        for i in self.graph[v]: 
            if visited[i] == False: 
                self.dfsUtil(i, visited) 

    # The function to do DFS traversal. It uses 
    # recursive DFSUtil() 
    def DFS(self,v): 

        # Mark all the vertices as not visited 
        #creating a Visited list and initialising it with False
        visited = [False]*(len(self.graph)) 

        # Call the recursive helper function to print 
        # DFS traversal 
        self.dfsUtil(v,visited) 


g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 

print ("Following is DFS from (starting from vertex 2)")
g.DFS(2) 


# This code is contributed by Wilfredarin