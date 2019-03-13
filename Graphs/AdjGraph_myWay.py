class Node:
    def __init__(self,data):
        self.node = vertex
        self.next = None

class Graph:
    def __init__(self,capacity):
        self.vertices  = capacity
        self.graph = [None]*self.capacity

    def add_edge(self,src,dst):
        node = Node(dst)
        node.next = self.graph[src]
        #node ka next hai wo pura 
        #pehle wala src ka hissa hai
        #node-->[]

        #dst-->(at src jo value stored hai)[]
        self.graph[src] = node
       #graph --[src]-->node
       #and this node contains allthe other vertices
        #at src ---> dst stored

        ##lets make it pura
        ##its undirected
        #src and dst same for us
        node = Node(src)
        node.next = self.graph[dst]
        self.graph[dst] = node


        def print_graph(self):
            for i in range(self.vertices):
                print("Adjacency list of vertex {}\n head".format(i), end="") 
            temp = self.graph[i] 
            while temp: 
                print(" -> {}".format(temp.vertex), end="") 
                temp = temp.next
            print(" \n") 

graph = Graph(5) 
graph.add_edge(0, 1) 
"""
graph=[-1,-1,-1,-1,-1]
{1}-->{-1}
graph =[{1}-->{-1},-1,-1,-1,-1]

{0}-->{-1}
graph =[{1}-->{-1},{0}-->{-1},-1,-1,-1]




"""
graph.add_edge(0, 4) 
"""
graph =[{1}-->{-1},{0}-->{-1},-1,-1,-1]


{4}-->{{1}-->{-1}}
graph =[{4}-->{{1}-->{-1}},-1,-1,-1,-1]

{0}-->{-1}
graph =[{4}-->{{1}-->{-1}},-1,-1,-1,{0}-->{-1}]

"""

graph.add_edge(1, 2) 
graph.add_edge(1, 3) 
graph.add_edge(1, 4) 
graph.add_edge(2, 3) 
graph.add_edge(3, 4) 

graph.print_graph() 