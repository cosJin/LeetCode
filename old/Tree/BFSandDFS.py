def BFS(graph,start,end):
    queue = []
    queue.append([start])
    visited = ()
    visited.add(start)
    while queue:
        node = queue.pop()
        visited.add(node)

        process(node)
        nodes = generate_related_nodes(node)
        queue.push(node)
visited = ()
def DFS(node,visited)
    visited.add(node)
    #precess current node
    for next_node in node.children():
        if not next_node in visited:
               DFS(next_node,visited) 
                