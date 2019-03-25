from collections import defaultdict

class Graph:
    def __init__(self,vertices):
        self.size = vertices
        self.graph = defaultdict(list)

    def addEdge(self,src,dst):
        self.graph[src].append(dst)

    
    #for @2PASS
    def DFSutil(self,v,visited):
        #mark the current node as visited
        visited[v] = True
        #pintIt
        print("|"+str(v)+"        |")
        
        #DFS 
        for i in self.graph[v]:
            #for neighbour of node
            #dfs
            #if not visited then go further
            if visited[i] == False:
                self.DFSutil(i,visited)
        #if visted found stop exit man
    

    #for 1st PAsS
    def finishTime(self,v,visited,stack):
        #mark visited true
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self.finishTime(i,visited,stack)
            #11@if visited found then put it in stack
            #the parent node finished 
            #put in stack
            stack.append(v)
        #It finishes once all the path(nodes)connected to it visited 

    def reverse(self):
        g= Graph(self.size)

        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j,i)
        return g



    def SCC(self):
        

        #FIRST PASS @1
        
        stack = []
        #mark all the vertices as not visited
        visited = [False]*self.size
        #fill the vertices according to the finishing time
        for i in range(self.size):
            #for all nodes check if its unvisited
            if visited[i] == False:
                #go for the finishing time
                self.finishTime(i,visited,stack)
                #it does DFS if it finds a visited node
                #it puts the node in stack
                #not always we would find a visited node
        

        #SECOND PASS @2 


        # Create a reversed graph 
        gr = self.reverse()
        # Now process all vertices in order defined by Stack 
        #Mark all the vertices as not visited (For second DFS) 
        visited =[False]*(self.size)
        #reverse order mai graph kiya hai
        while stack:
            i = stack.pop() 
            if visited[i]==False:
                print("---> ^^@@^^ ") 
                gr.DFSutil(i,visited) 
                print("---> ^^@@^^ ")




g = Graph(5) 
g.addEdge(1, 0) 
g.addEdge(0, 2) 
g.addEdge(2, 1) 
g.addEdge(0, 3) 
g.addEdge(3, 4) 



g.SCC() 
#This code is contributed by wilfredarin 









