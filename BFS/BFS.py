graph={
    'S':['A','D'],
    'A':['S','D','B'],
    'D':['S','A','E'],
    'B':['A','E','C'],
    'E':['B','F'],
    'F':['E','G'],
    'C':['B'],
    'G':['F']
}


def bfs(graph, start, destination):
    pathes = [[start]]
    check = set()
    while pathes:
        path = pathes.pop(0)
        nextcheck = path[-1]
        if nextcheck in check: continue
        success = graph[nextcheck]
        for i in success:
            if i in path: continue
            new_path = path + [i]
            pathes.append(new_path)
            if i == destination:
                return new_path
        check.add(nextcheck)

print(bfs(graph, 'S', 'G'))