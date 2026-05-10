from collections import deque

graph = {}

def add_edge(u, v):
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []

    graph[u].append(v)
    graph[v].append(u)

def dfs(node, visited=set()):
    visited.add(node)
    print(node, end=" ")

    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(neighbour, visited)

def bfs(start):
    visited = set([start])
    queue = deque([start])

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

n = int(input("Enter number of edges: "))

for i in range(n):
    u = input("Enter first vertex: ")
    v = input("Enter second vertex: ")
    add_edge(u, v)

print("Graph:", graph)

start = input("Enter starting node: ")

print("DFS:")
dfs(start)

print("\nBFS:")
bfs(start)
