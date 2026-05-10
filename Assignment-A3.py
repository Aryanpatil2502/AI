def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    print("Sorted Array:", arr)

def prim(graph, n):
    visited = [0]

    print("\nEdges in MST:")

    while len(visited) < n:
        minimum = 999
        x = y = 0

        for i in visited:
            for j in range(n):
                if j not in visited and graph[i][j] != 0:
                    if graph[i][j] < minimum:
                        minimum = graph[i][j]
                        x, y = i, j

        print(x, "-", y, "=", graph[x][y])
        visited.append(y)

while True:
    print("\n1. Selection Sort")
    print("2. Prim's Algorithm")
    print("3. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        arr = list(map(int, input("Enter numbers: ").split()))
        selection_sort(arr)

    elif choice == 2:
        n = int(input("Enter number of vertices: "))
        graph = []
        print("Enter adjacency matrix:")
        for i in range(n):
            row = list(map(int, input().split()))
            graph.append(row)

        prim(graph, n)

    elif choice == 3:
        break
