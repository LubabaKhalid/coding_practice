from collections import deque

# BFS Implementation
def bfs(graph, start):
    visited = set()  # Set to keep track of visited nodes
    queue = deque([start])  # Queue for BFS
    visited.add(start)

    while queue:
        node = queue.popleft()  # Get the node from the front of the queue
        print(node, end=" ")  # Process the node
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example usage
graph = {
    1: [3,2],
    2: [1, 5,4],
    3: [1],
    4: [2],
    5: [2]
}

bfs(graph, 1)  # Starting BFS from node 1
