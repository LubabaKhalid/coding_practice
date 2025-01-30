# DFS Implementation (Iterative)
def dfs(graph, start):
    visited = set()
    stack = [start]  # Stack for DFS
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node, end=" ")  # Process the node
            # Push all neighbors to the stack
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)

# Example usage
graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1],
    4: [2],
    5: [2]
}

dfs(graph, 1)  # Starting DFS from node 1
