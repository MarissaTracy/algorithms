#Marissa Tracy
#Problem 4
#import networkx as nx

#G=nx.DiGraph()
#G.add_weighted_edges_from(elist)

dependencyDict = { 'A': ['D'], 'B': ['A', 'E'], 'C': ['B'], 'D': ['C'], 'G':['H'] }
chainsDict = {}

for key in dependencyDict:
    currKey = key
    frontier = [key]
    visited = []
    while frontier:
        currKey = frontier[0]
        frontier.remove(currKey)
        if dependencyDict.get(currKey,0) and (currKey not in visited) and (currKey not in frontier):
            nodes = dependencyDict[currKey]
            frontier.extend(nodes)
            visited.append(currKey)
        elif currKey in visited:
            visited.remove(currKey)
        elif dependencyDict.get(currKey,0) == 0:
            visited.append(currKey)
    for i in visited:
        if i == key:
            visited.remove(i)
    chainsDict[key] = visited

print chainsDict
