#   Created by Roshan Jayswal 
#   Copyright © 2021 AppMillers. All rights reserved.

class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)
    
    def checkRoute(self, startNode, endNode):
        visited = [startNode]
        queue = [startNode]
        path = False
        while queue:
            deVertex = queue.pop(0)
            for adjacentVertex in self.gdict[deVertex]:
                if adjacentVertex not in visited:
                    if adjacentVertex == endNode:
                        path = True
                        break
                    else:
                        visited.append(adjacentVertex)
                        queue.append(adjacentVertex)
        return path
 



customDict = { "a" : ["c","d", "b"],
            "b" : ["j"],
            "c" : ["g"],
            "d" : [],
            "e" : ["f", "a"],
            "f" : ["i"],
            "g" : ["d", "h"],
            "h" : [],
            "i" : [],
            "j" : []
               }



g = Graph(customDict)
print(g.checkRoute("a", "j"))

