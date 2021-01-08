# -*- coding: utf-8 -*-
# 主题：基于递归的深度受限的搜索算法的简单实现

from pandas import DataFrame

# 城市信息：city1 city2 path_cost
_city_info = None

# 已探索集合
_explored = set()

# 节点数据结构
class Node:
    def __init__(self, state, parent, action, path_cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

def main():
    global _city_info, _explored
    import_city_info()

    while True:
        src_city = input('input src city\n')
        if src_city == 'quit':
            break
        dst_city = input('input dst city\n')
        limit = int(input('input limit\n'))
        result = depth_limited_search(src_city, dst_city, limit)
        if result == "failure" or result == "cutoff":
            print('from city: %s to city %s search failure' % (src_city, dst_city))
        else:
            print('from city: %s to city %s search success' % (src_city, dst_city))
            path = []
            while True:
                path.append(result.state)
                if result.parent is None:
                    break
                result = result.parent
            size = len(path)
            for i in range(size):
                if i < size - 1:
                    print('%s->' % path.pop(), end='')
                else:
                    print(path.pop())

def import_city_info():
    global _city_info
    data = [{'city1': 'Oradea', 'city2': 'Zerind', 'path_cost': 71},
            {'city1': 'Oradea', 'city2': 'Sibiu', 'path_cost': 151},
            {'city1': 'Zerind', 'city2': 'Arad', 'path_cost': 75},
            {'city1': 'Arad', 'city2': 'Sibiu', 'path_cost': 140},
            {'city1': 'Arad', 'city2': 'Timisoara', 'path_cost': 118},
            {'city1': 'Timisoara', 'city2': 'Lugoj', 'path_cost': 111},
            {'city1': 'Lugoj', 'city2': 'Mehadia', 'path_cost': 70},
            {'city1': 'Mehadia', 'city2': 'Drobeta', 'path_cost': 75},
            {'city1': 'Drobeta', 'city2': 'Craiova', 'path_cost': 120},
            {'city1': 'Sibiu', 'city2': 'Fagaras', 'path_cost': 99},
            {'city1': 'Sibiu', 'city2': 'Rimnicu Vilcea', 'path_cost': 80},
            {'city1': 'Rimnicu Vilcea', 'city2': 'Craiova', 'path_cost': 146},
            {'city1': 'Rimnicu Vilcea', 'city2': 'Pitesti', 'path_cost': 97},
            {'city1': 'Craiova', 'city2': 'Pitesti', 'path_cost': 138},
            {'city1': 'Fagaras', 'city2': 'Bucharest', 'path_cost': 211},
            {'city1': 'Pitesti', 'city2': 'Bucharest', 'path_cost': 101},
            {'city1': 'Bucharest', 'city2': 'Giurgiu', 'path_cost': 90},
            {'city1': 'Bucharest', 'city2': 'Urziceni', 'path_cost': 85},
            {'city1': 'Urziceni', 'city2': 'Vaslui', 'path_cost': 142},
            {'city1': 'Urziceni', 'city2': 'Hirsova', 'path_cost': 98},
            {'city1': 'Neamt', 'city2': 'Iasi', 'path_cost': 87},
            {'city1': 'Iasi', 'city2': 'Vaslui', 'path_cost': 92},
            {'city1': 'Hirsova', 'city2': 'Eforie', 'path_cost': 86}]
    _city_info = DataFrame(data, columns=['city1', 'city2', 'path_cost'])

def depth_limited_search(src_state, dst_state, limit):
    global _explored
    _explored = []
    node = Node(src_state, None, None, 0)
    return recursive_dls(node, dst_state, limit)

def recursive_dls(node, dst_state, limit):
    """
        :param node:
        :param dst_state:
        :param limit:
        :return: "failure"：失败."cutoff"：被截至.node：成功
        """
    global _city_info, _explored

    if node.parent is not None:
        print('node state:%s parent state:%s' % (node.state, node.parent.state))
    else:
        print('node state:%s parent state:%s' % (node.state, None))

    # 目标测试
    if node.state == dst_state:
        print('this node is goal!')
        return node
    elif limit == 0:
        print('this node is cutoff!')
        return "cutoff"
    else:
        cutoff_occurred = False

        # 遍历子节点
        for i in range(len(_city_info)):
            dst_city = ''
            if _city_info['city1'][i] == node.state:
                dst_city = _city_info['city2'][i]
            elif _city_info['city2'][i] == node.state:
                dst_city = _city_info['city1'][i]
            if dst_city == '':
                continue
            child = Node(dst_city, node, 'go', node.path_cost + _city_info['path_cost'][i])
            # 过滤已探索的点
            if child.state in _explored:
                continue
            print('child node:state:%s path cost:%d' % (child.state, child.path_cost))
            # 递归的方法，把当前child返回，并且limit-1
            _explored.append(node.state)
            result = recursive_dls(child, dst_state, limit - 1)
            if result == "cutoff":
                cutoff_occurred = True
                print('search failure, child state: %s parent state: %s limit cutoff' %
                      (child.state, child.parent.state))
            elif result != "failure":
                print('search success')
                return result
        if cutoff_occurred:
            return "cutoff"
        else:
            return "failure"

if __name__ == '__main__':
    main()