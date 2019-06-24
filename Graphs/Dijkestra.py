from collections import defaultdict


class Graph:
	def __init__(self,size):
		self.size = size
		self.graph = defaultdict(list)
		self.cost = [[ [0] for i in range(self.size)] for i in range(self.size)]

	def add_edge(self,frm,to,length =0):
		self.graph[frm].append(to)
		self.graph[to].append(frm)
		self.cost[frm][to] = length
		self.cost[to][frm] = length
		

	def dijkestra(self,src):
		dist = [float("inf")]*self.size
		prev = [-1]*self.size

		Q = []*self.size
		for i in self.graph:
			Q.append(i)
		dist[src] = 0

		while Q:
			min_ = dist[Q[0]]
			u = Q[0]
			for i in Q:
				if dist[i]<min_:
					min_ = dist[i]
					u = i
			Q.remove(u)
            

			for i in self.graph[u]:
				alt = dist[u] + self.cost[u][i]
				if alt < dist[i]:
					dist[i] = alt
					prev[i] = u
		for i in range(self.size):
			print("vertex "+str(i) +" is at a distance of " +str(dist[i]) )
	

g = Graph(9)
g.add_edge(0,1,4)
g.add_edge(0,7,8)
g.add_edge(1,2,8)
g.add_edge(1,7,11)
g.add_edge(7,8,7)
g.add_edge(7,6,1)
g.add_edge(8,2,2)
g.add_edge(8,6,6)
g.add_edge(6,5,2)
g.add_edge(2,5,4)
g.add_edge(2,3,7)
g.add_edge(3,4,9)
g.add_edge(3,5,14)
g.add_edge(5,4,10)
g.dijkestra(0)


#wilfredarin
#pseudocode on wikki :https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm