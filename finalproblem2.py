#!/usr/bin/env python

class Edge(object):
  def __init__(self, u, v, w):
    self.source = u
    self.target = v
    self.capacity = w

  def __repr__(self):
    return "%s->%s:%s" % (self.source, self.target, self.capacity)


class FlowNetwork(object):
  def  __init__(self):
    self.adj = {}
    self.flow = {}

  def AddVertex(self, vertex):
    self.adj[vertex] = []

  def GetEdges(self, v):
    return self.adj[v]

  def AddEdge(self, u, v, w = 0):
    if u == v:
      raise ValueError("u == v")
    edge = Edge(u, v, w)
    redge = Edge(v, u, 0)
    edge.redge = redge
    redge.redge = edge
    self.adj[u].append(edge)
    self.adj[v].append(redge)
    # Intialize all flows to zero
    self.flow[edge] = 0
    self.flow[redge] = 0

  def FindPath(self, source, target, path):
    if source == target:
      return path
    for edge in self.GetEdges(source):
      residual = edge.capacity - self.flow[edge]
      if residual > 0 and not (edge, residual) in path:
        result = self.FindPath(edge.target, target, path + [(edge, residual)])
        if result != None:
          return result

  def MaxFlow(self, source, target):
    path = self.FindPath(source, target, [])
    print 'path after enter MaxFlow: %s' % path
    for key in self.flow:
      print '%s:%s' % (key,self.flow[key])
    print '-' * 20
    while path != None:
      flow = min(res for edge, res in path)
      for edge, res in path:
        self.flow[edge] += flow
        self.flow[edge.redge] -= flow
      for key in self.flow:
        print '%s:%s' % (key,self.flow[key])
      path = self.FindPath(source, target, [])
      print 'path inside of while loop: %s' % path
    for key in self.flow:
      print '%s:%s' % (key,self.flow[key])
    return sum(self.flow[edge] for edge in self.GetEdges(source))


if __name__ == "__main__":
  #create a directed graph
  G = nx.DiGraph()

  #adding an edge also adds the node
  G.add_edge('Spider', 'A', weight=1.0)
  G.add_edge('Spider', 'H', weight=1.0)
  G.add_edge('Spider', 'J', weight=1.0)

  G.add_edge('H', 'G', weight=1.0)
  G.add_edge('H', 'K', weight=1.0)

  G.add_edge('G', 'L', weight=1.0)
  G.add_edge('G', 'F', weight=1.0)

  G.add_edge('F', 'E', weight=1.0)

  G.add_edge('E', 'Fly', weight=1.0)

  G.add_edge('J', 'S', weight=1.0)
  G.add_edge('J', 'K', weight=1.0)

  G.add_edge('K', 'L', weight=1.0)
  G.add_edge('L', 'M', weight=1.0)
  G.add_edge('M', 'N', weight=1.0)
  G.add_edge('M', 'F', weight=1.0)

  G.add_edge('N', 'O', weight=1.0)
  G.add_edge('N', 'E', weight=1.0)

  G.add_edge('O', 'Fly', weight=1.0)

  G.add_edge('A', 'S', weight=1.0)
  G.add_edge('A', 'B', weight=1.0)

  G.add_edge('B', 'R', weight=1.0)
  G.add_edge('B', 'C', weight=1.0)

  G.add_edge('S', 'R', weight=1.0)
  G.add_edge('R', 'Q', weight=1.0)

  G.add_edge('Q', 'C', weight=1.0)
  G.add_edge('Q', 'P', weight=1.0)

  G.add_edge('C', 'D', weight=1.0)
  G.add_edge('D', 'Fly', weight=1.0)
  G.add_edge('P', 'D', weight=1.0)
  G.add_edge('P', 'O', weight=1.0)
  G.add_edge('O', 'Fly', weight=1.0)

  G.add_edge('T', 'Q', weight=1.0)
  G.add_edge('T', 'P', weight=1.0)
  G.add_edge('T', 'O', weight=1.0)
  G.add_edge('T', 'N', weight=1.0)
  G.add_edge('T', 'M', weight=1.0)

  G.add_edge('R', 'T', weight=1.0)
  G.add_edge('S', 'T', weight=1.0)
  G.add_edge('J', 'T', weight=1.0)
  G.add_edge('K', 'T', weight=1.0)
  G.add_edge('L', 'T', weight=1.0)

  #each edge has a weight of 1. The shortest path is the fewest edges.
  #Use this to verify that your graph built correctly.
  t = nx.shortest_path(G, 'Spider', 'Fly', weight='weight')
