class Node(object):

    def __init__(self, label):
        self.label = label
        self.children = []

    def __repr__(self):
        """Return a string form of this node."""
        return '{} -> {}'.format(self.label, self.children)

    def add_child(self, nodes, cost=1):
        if type(nodes) is list:
            [self.add_child(node) for node in nodes]
            return
        edge = Edge(self, nodes, cost)
        self.children.append(edge)

class Edge(object):

    def __init__(self, src:Node, dest:Node, cost:int):
        self.src = src
        self.dest = dest
        self.cost = cost

    def __repr__(self):
        """Return a string form of this edge."""
        return '{}: {}'.format(self.dest.label, self.cost)
