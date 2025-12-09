import heapq

# Weighted graph (adjacency list)
graph = {
    'A': [('B', 2), ('C', 5)],
    'B': [('C', 1), ('D', 4)],
    'C': [('D', 1)],
    'D': [('E', 3)],
    'E': []
}

# Uniform-Cost Search
def ucs(graph, start, goal):
    pq = [(0, start, [start])]
    visited = set()
    while pq:
        cost, node, path = heapq.heappop(pq)
        if node in visited:
            continue
        visited.add(node)
        if node == goal:
            return cost, path
        for nxt, w in graph[node]:
            if nxt not in visited:
                heapq.heappush(pq, (cost + w, nxt, path + [nxt]))
    return float('inf'), []

# Dijkstra (for validation)
def dijkstra(graph, start, goal):
    pq = [(0, start)]
    dist = {n: float('inf') for n in graph}
    parent = {n: None for n in graph}
    dist[start] = 0
    while pq:
        cost, node = heapq.heappop(pq)
        if node == goal:
            break
        for nxt, w in graph[node]:
            if cost + w < dist[nxt]:
                dist[nxt] = cost + w
                parent[nxt] = node
                heapq.heappush(pq, (dist[nxt], nxt))
    path = []
    cur = goal
    while cur:
        path.append(cur)
        cur = parent[cur]
    return dist[goal], path[::-1]

# Run and compare
start, goal = 'A', 'E'
ucs_cost, ucs_path = ucs(graph, start, goal)
d_cost, d_path = dijkstra(graph, start, goal)

print("UCS:", ucs_path, "Cost:", ucs_cost)
print("Dijkstra:", d_path, "Cost:", d_cost)
print("Optimal:", "YES" if ucs_cost == d_cost else "NO")
