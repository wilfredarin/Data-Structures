from collections import defaultdict
t = int(input())
for i in range(t):
	v,e = map(int,input().split())
	graph = defaultdict(list)
	
	for i in range(e):
		s,d = map(int,input().split())
		graph[s].append(d)
		graph[d].append(s)

	
	for i in range(v):
		s=""
		s+=str(i)
		for j in graph[i]:
		    s+="->"+str(j)
		print(s)
		
		
		
		


