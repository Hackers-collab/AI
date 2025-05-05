# Double ended Queue
from collections import deque

# Recursive DFS
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    print(node, end=' ')

    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Recursive BFS
def bfs_recursive(graph, queue, visited):

    # If There are no more nodes to visit stop the recurssion(Base Case)
    if not queue:
        return

    next_level = deque() # hold the neighbors of the node in queue

    while queue:

        # Remove a node from a current level and print it
        vertex = queue.popleft()
        print(vertex, end=' ')

        # For each node of the current node 
        # - If it hasn't been visited
        # - mark it as visited 
        # - Add to next level to process it
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                next_level.append(neighbor)

    bfs_recursive(graph, next_level, visited)


# Main function
def main():
    graph = {}

    # Take input
    n = int(input("Enter number of vertices: "))
    e = int(input("Enter number of edges: "))

    print("Enter edges (format: node1 node2):")
    for _ in range(e):
        u, v = input().split()
        # Undirected graph: Add both directions
        graph.setdefault(u, []).append(v)
        graph.setdefault(v, []).append(u)

    start_node = input("Enter the starting node: ")

    print("\nDepth First Search (DFS) - Recursive:")
    dfs(graph, start_node)

    print("\nBreadth First Search (BFS) - Recursive:")
    visited_bfs = set([start_node])
    queue = deque([start_node])
    bfs_recursive(graph, queue, visited_bfs)

main()
