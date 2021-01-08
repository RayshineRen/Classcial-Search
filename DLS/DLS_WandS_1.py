# -*- coding: utf-8 -*-
# Python版本：3.6

'''
3只羊和3头狼在河岸A，想要过河抵达河岸B。它们只有一艘船并且船上必须有1-2只生物。当

任意一边的狼的数量大于羊时，羊会被吃光（fail）。初始状态为（3,3,1,0,0,0），意为3头羊

，3头狼和一艘船在河岸A，而河岸B没有羊，没有狼，也没有船。算法程序要达成的目标是（

0,0,0,3,3,1），意为3头羊，3头狼和一艘船都从河岸A抵达了河岸B。请用深度受限搜索（

Depth-Limited-Search）完成这份python程序，受限深度为15。
'''

# 已探索集合
_explored = []

action = [[0, -1, 0], [0, -2, 0], [-1, 0, 0], [-2, 0, 0], [-1, -1, 0], [0, 1, 1], [0, 2, 1], [1, 0, 1], [2, 0, 1],
          [1, 1, 1]]


# 节点数据结构
class Node:
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


def main():
    global _explored

    src_state = [3, 3, 1, 0, 0, 0]
    dst_state = [0, 0, 0, 3, 3, 1]
    limit = 15

    result = depth_limited_search(src_state, dst_state, limit)
    if result == "failure" or result == "cutoff":
        print('from src_state: %s to dst_state %s search failure' % (src_state, dst_state))
    else:
        print('from src_state: %s to dst_state %s search success' % (src_state, dst_state))
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


def depth_limited_search(src_state, dst_state, limit):
    global _explored
    _explored = []
    node = Node(src_state, None, None)
    return recursive_dls(node, dst_state, limit)


def recursive_dls(node, dst_state, limit):
    """
        :param node:
        :param dst_state:
        :param limit:
        :return: "failure"：失败."cutoff"：被截至.node：成功
        """
    global _explored

    if node.parent is not None:
        print('node state:%s parent state:%s' % (node.state, node.parent.state))
    else:
        print('node state:%s parent state:%s' % (node.state, None))
    _explored.append(node.state)

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
        for state in action:
            if node.state[5] == state[2] and (node.state[1] + state[1]) >= 0 and (
                    node.state[1] + state[1]) <= 3 \
                    and (node.state[0] + state[0]) >= 0 and (node.state[0] + state[0]) <= 3:
                left_sheep = node.state[0] + state[0]
                left_wolf = node.state[1] + state[1]
                right_sheep = node.state[3] - state[0]
                right_wolf = node.state[4] - state[1]
                next_state = list(node.state)

                if (left_sheep == 0 or (left_sheep > 0 and left_sheep >= left_wolf)) and \
                        (right_sheep == 0 or (right_sheep > 0 and right_sheep >= right_wolf)):
                    next_state[0] = left_sheep
                    next_state[1] = left_wolf
                    next_state[2] = int(node.state[5])
                    next_state[3] = right_sheep
                    next_state[4] = right_wolf
                    next_state[5] = int(not (node.state[5]))

                    child = Node(next_state, node, 'do')
                    # 过滤已探索的点
                    if child.state in _explored:
                        continue
                    print('child node:state:%s ' % (child.state))
                    # 递归的方法，把当前child返回，并且limit-1
                    result = recursive_dls(child, dst_state, limit - 1)
                    if result == "cutoff":
                        cutoff_occurred = True
                        print('search failure, child state: %s parent state: %s limit cutoff' %
                              (child.state, child.parent.state))
                    elif result != "failure":
                        print('search success')
                        print("At the currnet", node.state, "you will take the action", state,
                              "and then,your new state is ", child.state)
                        return result
        if cutoff_occurred:
            return "cutoff"
        else:
            return "failure"


if __name__ == '__main__':
    main()