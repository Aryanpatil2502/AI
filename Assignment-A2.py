import heapq

goal = [[1,2,3],[4,5,6],[7,8,0]]
dirs = [(-1,0),(1,0),(0,-1),(0,1)]

def h(state): return sum(state[i][j] != 0 and state[i][j] != goal[i][j] for i in range(3) for j in range(3))
def blank(state): return next((i,j) for i in range(3) for j in range(3) if state[i][j]==0)
def to_tuple(state): return tuple(tuple(r) for r in state)

def a_star(start):
    pq = [(h(start), 0, start, [])]
    visited = set()
    while pq:
        f, g, cur, path = heapq.heappop(pq)
        if to_tuple(cur) in visited: continue
        visited.add(to_tuple(cur))
        if cur == goal: return path + [cur]
        x, y = blank(cur)
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if 0<=nx<3 and 0<=ny<3:
                ns = [r[:] for r in cur]
                ns[x][y], ns[nx][ny] = ns[nx][ny], ns[x][y]
                if to_tuple(ns) not in visited:
                    ng = g+1
                    heapq.heappush(pq, (ng+h(ns), ng, ns, path+[cur]))
    return None

def get_input():
    print("Enter initial state (0=blank):")
    return [[int(n) for n in input(f"Row {i+1}: ").split()] for i in range(3)]

path = a_star(get_input())
if path:
    [print(f"Step {i}:\n"+"\n".join(str(r) for r in s)+"\n") for i, s in enumerate(path)]
else:
    print("No solution found.")
