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

visited = set()                          # list to keep track of visited nodes.
                            

def dfs (visited,graph,node):
    if node not in visited:
        visited.add(node)
        print(node)
        for neighbour in graph[node]:
            dfs(visited,graph,neighbour)


dfs(visited,graph,'A')                #calling function