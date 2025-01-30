# DFS Implementation (Recursive)
def dfs(graph, node, visited):
    visited.add(node)  # Mark the node as visited
    print(node, end=" ")  # Process the node
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example usage
graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1],
    4: [2],
    5: [2]
}

visited = set()
dfs(graph, 1, visited)  # Starting DFS from node 1
