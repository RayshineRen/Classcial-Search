from queue import PriorityQueue

queue = PriorityQueue()
queue.put((2, 'A'))
queue.put((3, 'B'))
queue.put((1, 'C'))

cost, node = queue.get()
l = list(queue)
print(l)
print(cost, ',', node)

q = PriorityQueue()
# 格式：q.put((数字,值))
#特点：数字越小，优先级越高
c = [6,3,7,5,0,2]
for i in c:
    q.put([i,10])
b = q.get()
print(b)
#[0, 10]
b = q.get()
print(b)
# [2, 10]
b = q.get()
print(b)
# [3, 10]
b = q.get()
print(b)
# [5, 10]
b = q.get()
print(b)
# [6, 10]
b = q.get()
print(b)
# [7, 10]

# q = PriorityQueue()
# c = [6,3,7,5,0,2]
# for i in c:
#     q.put([i,10])
# c = q.queue
# print(c)
# #[[0, 10], [3, 10], [2, 10], [6, 10], [5, 10], [7, 10]]并不按照优先级
# while len(q.queue) > 5:
#     q.get()
# print(c)

# q = PriorityQueue()
# c = [6,3,7,5,0,2]
# for i in c:
#     q.put([i,10])
# i = 0
# while i < q.qsize():#循环，q.qsize()为队列大小
#     c = q.get()
#     print(c)
# print(q.queue)

# !usr/bin/env python
# -*- coding:utf-8 _*-

import queue
import threading
import time

# q = queue.PriorityQueue()
# q.put([1, 'ace'])
# q.put([40, 333])
# q.put([3, 'afd'])
# q.put([5, '4asdg'])
# # 1是级别最高的，
# while not q.empty():  # 不为空时候执行
#     print(q.get())
#
# q = queue.PriorityQueue()
# q.put('我')
# q.put('你')
# q.put('他')
# q.put('她')
# q.put('ta')
# print(q.queue)
# while not q.empty():
#     print(q.get())
