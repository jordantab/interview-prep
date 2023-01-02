
# Cracking the Coding Interview: Trees and Graphs 4.1
# Problem: Given a directed graph and two nodes S and E, design an algorithm to find out whether there is a route from S to E.
# Author: Jordan Tab

# Logic: run DFS from S and see if E is visited

graph1 = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : ['D']
}

visited = set()

def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs(visited, graph, neighbor)

def pathfinder(node, target, visited, graph):
    dfs(visited, graph, node)
    return (target in visited)

print(pathfinder('C', 'E', visited, graph1))