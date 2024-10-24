def build_graph(edges):
    graph = {}
    for parent, child in edges:
        if parent not in graph:
            graph[parent]= []
        graph[parent].append(child)
    return graph