graph = {
    'A':['B','C'],
    'B':['A','C','D'],
    'C':['A','B','D','E'],
    'D':['B','C','E','F'],
    'E':['C','D'],
    'F':['D']
}

Goal_Node = 'F'

def BFSGraph(graph, inital_node):
    node = inital_node
    # print(node)
    solution = [node]
    if node == Goal_Node:
        return solution
    frontier = list()
    frontier.append(node)
    explored = set()
    while True:
        if len(frontier)<=0:
            return False
        node = frontier.pop()
        explored.add(node)
        print(node)
        for childNode in graph[node]:
            if not childNode in explored and not childNode in frontier:
                # print(childNode)
                if childNode == Goal_Node:
                    print(Goal_Node)
                    return True
                frontier.append(childNode)
print(BFSGraph(graph, 'A'))