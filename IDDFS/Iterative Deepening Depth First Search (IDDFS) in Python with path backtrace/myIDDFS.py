from DataStructure import *

A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')
G = Node('G')

A.add_child([B, C, E])
B.add_child([A, D, F])
C.add_child([G, A])
D.add_child(B)
E.add_child([F, A])
F.add_child([E, B])
G.add_child(C)

def IDDFS(root:Node, goal:str, maximum_depth:int=10):
    for depth in range(0, maximum_depth):
        explored = set()
        result = DLS([root], goal, depth, explored)
        if result is None:
            continue
        return result

    raise ValueError('goal not in graph with depth {}'.format(maximum_depth))

def DLS(path:list, goal:str, depth:int, explored):
    cur = path[-1]
    # print(cur)
    if cur.label == goal:
        return path
    if depth <= 0:
        return None
    for edge in cur.children:
        new_path = path+[edge.dest]
        result = DLS(new_path, goal, depth-1, explored)
        if result is not None:
            return result
    explored.add(cur)

# print(A.children)
result = IDDFS(D, 'G')
for node in result:
    print(node.label+"->",end='')
print('Goaaaaaal!')


