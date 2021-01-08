from DataStructure import *
from queue import PriorityQueue

A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
G = Node('G')

A.add_child(B, 1)
A.add_child(C, 2)
B.add_child(A, 1)
B.add_child(D, 3)
C.add_child(A, 2)
C.add_child(E, 1)
D.add_child(B, 3)
D.add_child(G, 2)
E.add_child(C, 1)
E.add_child(G, 4)
G.add_child(D, 2)
G.add_child(E, 4)

def UCS(root:Node, Goal:str):
    frontier = PriorityQueue()
    explored = set()
    frontier.put((0, [root]))
    while True:
        if(frontier.qsize() <= 0):
            return False
        accu_cost, path = frontier.get()
        cur = path[-1]
        if cur.label == Goal:
            return (accu_cost, path)
        for child in cur.children:
            cur_cost = accu_cost+child.cost
            cur_path = path+[child.dest]
            if not cur_path[-1] in explored:
                frontier.put((cur_cost, cur_path))
        explored.add(cur)

cost, path = UCS(A, 'G')
if path!=False:
    for node in path:
        print(node.label+"->",end="")
    print("Gooooal! with cost is ",cost)

