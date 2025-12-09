from collections import deque
# Graph and heuristic
graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'D': 3, 'E': 2},
    'C': {'F': 3},
    'D': {'G': 4},
    'E': {'G': 5},
    'F': {'G': 1},
    'G': {}
}
h = {'A':7,'B':5,'C':4,'D':2,'E':3,'F':1,'G':0}
# Beam Search
def beam_search(start, goal, k):
    frontier = [(h[start], [start])]
    while frontier:
        nxt = []
        for _, path in frontier:
            node = path[-1]
            if node == goal:
                return path
            for n in graph[node]:
                nxt.append((h[n], path+[n]))
        if not nxt:
            return None
        nxt.sort(key=lambda x: x[0])
        frontier = nxt[:k]
    return None
# BFS for comparison
def bfs(start, goal):
    q = deque([[start]])
    vis = set()
    while q:
        path = q.popleft()
        node = path[-1]
        if node == goal:
            return path
        if node not in vis:
            vis.add(node)
            for n in graph[node]:
                q.append(path+[n])
    return None
# Run
start, goal, k = 'A', 'G', 2
bp = beam_search(start, goal, k)
bf = bfs(start, goal)
print("Beam Search:", bp)
print("BFS:", bf)
print("Beam missed optimal path?" , bp != bf)
