from collections import deque

graph = {}

n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input("Enter node name: ").strip()
    edges = input(f"Enter edges for {node}: ").split()

    graph[node] = edges

    # Ensure all mentioned nodes exist in graph
    for e in edges:
        if e not in graph:
            graph[e] = []

start = input("Enter starting node: ").strip()

def bfs(start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()   # Remove from front (FIFO)
        
        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            for x in graph[node]:
                if x not in visited:
                    queue.append(x)

bfs(start)