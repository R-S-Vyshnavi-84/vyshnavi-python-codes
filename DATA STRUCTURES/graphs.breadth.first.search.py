graph = {
    'A' : ['B','C'],
    'B' : ['D','E'],
    'C' : ['F','G'],
    'D' : [],
    'E' : ['H'],
    'F' : [],
    'G' : [],
    'H' : [],
}

visited = []                            # list to keep track of visited nodes.
queue = []                              # initialize the queue   

def bfs (visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue:
        s=queue.pop(0)
        print(s,'->',end=' ')
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


bfs(visited,graph,'A')                #calling function