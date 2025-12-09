from collections import deque

start = (3, 3, 'left')
goal = (0, 0, 'right')

def valid(m, c):
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False
    m_r, c_r = 3 - m, 3 - c
    if (m > 0 and c > m) or (m_r > 0 and c_r > m_r):
        return False
    return True

def successors(state):
    m, c, boat = state
    moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]
    succ = []

    for mm, cc in moves:
        if boat == 'left':
            ns = (m-mm, c-cc, 'right')
        else:
            ns = (m+mm, c+cc, 'left')

        if valid(ns[0], ns[1]):
            succ.append(ns)

    return succ

def bfs(start, goal):
    q = deque([(start, [start])])
    vis = set()

    while q:
        state, path = q.popleft()
        if state == goal:
            return path
        vis.add(state)

        for s in successors(state):
            if s not in vis:
                q.append((s, path + [s]))
    return None

sol = bfs(start, goal)

if sol:
    print("Solution Found:")
    for step in sol:
        print(step)
else:
    print("No solution.")
