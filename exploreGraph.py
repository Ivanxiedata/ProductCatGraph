from productinfo import input
def dfs(graph, curr_node, curr_path, all_paths):

    # Add current node to the path
    curr_path.append(curr_node)

    # If current node has no children, it's a leaf, so we save the current path
    if curr_node not in graph or not (graph[curr_node]):
        all_paths.append(curr_path.copy())  # Copy to avoid mutability issues
    else:
        # Recur for all the children
        for child in graph[curr_node]:
            dfs(graph, child, curr_path, all_paths)

    # Backtrack to explore other paths
    curr_path.pop()

def exploreGraph(start_category):

    # All paths will be stored here
    all_paths = []
    curr_path = []

    # Call DFS to find all paths from start_category
    dfs(input, start_category, curr_path, all_paths)

    return all_paths
