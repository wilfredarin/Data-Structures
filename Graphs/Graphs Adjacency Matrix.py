"""  
what is graph :-> 
	
	non-linear data structure
	consisting of nodes and edges. 
	The nodes : vertices  
	 the edges:  lines or arcs that
	  connect any two nodes. 

Graph consists of a finite set of vertices(or nodes) and set of Edges which connect a pair of nodes


two most commonly used representations of a graph.
1. Adjacency Matrix
2. Adjacency List



Adjacency Matrix: 
2D array of size V x V where V is the number of vertices in a graph.

Let the 2D array be adj[][], 
a slot adj[i][j] = 1 
indicates that there is an edge from vertex i to vertex j.


ADJACENCY GRAPH FOR UNDIRECTED GRAPH ALways symmetric.

 If adj[i][j] = w, 
 then there is an edge from vertex i to vertex j with weight w.



pros:
 	O(1) : look up,removing
cons:
	more space,even if less edges




"""


#A simple representation of graph using Adjacency Matrix
#Graph class
#	numvertex,adjMatrix,vertives,verticeslist
#   set_vertex,set_edge:adjMatrix,get_vertex,get_edge
class Graph:
    def __init__(self,numvertex):
        self.adjMatrix = [[-1]*numvertex for x in range(numvertex)]
        #creates a 2d array ([-1 -1 -1],[-1 -1 -1],[-1 -1 -1 ])
        self.numvertex = numvertex
        self.vertices = {}
        #empty dictionary 
        self.verticeslist =[0]*numvertex #list of vertices in the graph
#set_vertex method  has 2 arg : index and Name of the vertex:

    def set_vertex(self,vtx,id):
        if 0<=vtx<=self.numvertex:
        	#id is the name of the vertex: vtx is the index of the vertex
            self.vertices[id] = vtx 
            self.verticeslist[vtx] = id #at vtx pos place the vertex name in the list

#edge: src dest cost(weight)
#it sets frm=value at vertices[in from Name what ever stored] --- these re indices of the name(number)
#it sets to = value at vertices[in to Name what ever stored]
#in adjMatrix set it 

    def set_edge(self,frm,to,cost=0):
        frm = self.vertices[frm]
        to = self.vertices[to]
        self.adjMatrix[frm][to]=cost
        #for directed graph do not add this
        self.adjMatrix[to][frm] = cost

    def get_vertex(self):
        return self.verticeslist
#edge has src dest  cost (src n dst from verticeslist..... ) and cost from adjMatrix
    def get_edges(self):
        edges=[]
        for i in range (self.numvertex):
            for j in range (self.numvertex):
                if (self.adjMatrix[i][j]!=-1):
                    edges.append((self.verticeslist[i],self.verticeslist[j],self.adjMatrix[i][j]))
                    #src dest weight
        return edges
        
    def get_matrix(self):
        return self.adjMatrix



print("Welcome to graphs!!")
n=int(input("please enter the number of vertices you want in your graph:"))
G =Graph(n)
for i in range(n):
	a=(input("please enter ->"+str(i+1)+ " vertex name Name:"))
	G.set_vertex(i,a)
print("Now set the Edges: input source-->Destination--->cost:")
for i in range(n-1):
	#n vertices has n-1 edge
	a,b,c=(input("source Destination Cost :").split(" "))
	G.set_edge(a,b,int(c))


print("Vertices of Graph")
print(G.get_vertex())
print("Edges of Graph")
print(G.get_edges())
print("Adjacency Matrix of Graph")
print(G.get_matrix())
print("test run")
print(G.vertices)
#This code is contributed by Sameer Ranjan
