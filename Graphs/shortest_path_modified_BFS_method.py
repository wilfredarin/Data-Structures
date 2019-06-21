from collections import defaultdict

class Graph:
	def __init__(self,size):
		self.graph = defaultdict(list)
		self.size = size

	def addEdge(self,frm,to):
		self.graph[frm].append(to)
		self.graph[to].append(frm)


	def shortest_path(self,s,dest):
		dist = [-1]*(self.size)
		prev = [-1]*(self.size)
		path=[]


		dist[s] = 0
		queue = [s]
		
		while queue:
			t = queue.pop(0)
			
			for i in self.graph[t]:
				if (dist[i] == -1):
					dist[i] = dist[t]+1
					prev[i] = t
					queue.append(i)
		
		path.append(dest)
		t = dest
		while prev[t]!=-1:
			path.append(prev[t])
			t =prev[t]
		
		path.reverse()
		print("Distance of "+ str(s)+" from  "+ str(dest)+" is :: "+str(dist[dest]))
		print("The Path is :: "+ '-> '.join(map(str,path)))

					
g = Graph(8)
g.addEdge(0,1)
g.addEdge(1,2)
g.addEdge(0,3)
g.addEdge(7,3)
g.addEdge(7,4)
g.addEdge(6,4)
g.addEdge(6,5)
g.addEdge(4,5)
g.addEdge(4,3)
g.addEdge(6,7)
g.shortest_path(0,7)
print(g.graph)