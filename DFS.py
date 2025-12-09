graph = {}

n = int(input("enter the nodes :\n"))  # number of nodes

for i in range(n):
    node = input().strip()
    edges = input().split()
    graph[node] = edges

    for e in edges:
        if e not in graph:
            graph[e] = []

start = input().strip()
visited = set()

def dfs(s):
    if s not in visited:
        print(s, end=" ")
        visited.add(s)
        for x in graph[s]:
            dfs(x)

dfs(start)

