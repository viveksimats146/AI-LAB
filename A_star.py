from heapq import heappush, heappop

# ---- INPUT ----
n = int(input("Enter number of nodes: "))
h = {}
for _ in range(n):
    x, y = input().split()
    h[x] = int(y)

e = int(input("Enter number of edges: "))
g = {}
for u in h.keys():
    g[u] = []

for _ in range(e):
    u, v, w = input().split()
    g[u].append((v, int(w)))

s = input("Enter start: ")
t = input("Enter goal: ")

# ---- A* SEARCH ----
pq = [(h[s], 0, s)]         # (f = g+h, g, node)
vis = set()

while pq:
    f, gc, u = heappop(pq)

    if u in vis:
        continue
    vis.add(u)

    if u == t:
        print("Cost =", gc)
        break

    for v, w in g[u]:
        heappush(pq, (gc + w + h[v], gc + w, v))
