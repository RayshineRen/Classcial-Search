# https://blog.csdn.net/marxoffice/article/details/97501536
n = 4
m = 4
H= [
     [1, 2, 3, 4],
     [5,6,7,8],
     [9,10,11,12],
     [13,14,15,16]
]
maxx = 0
maxy = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]  # 四个可能的方向
for i in range(n):  # 寻找最高点
    for j in range(m):
        if H[i][j] > H[maxx][maxy]:
            maxx = i
            maxy = j
temp = [maxx, maxy, 0]  # 第一个元素 起点坐标加初始路程
que = []
que.append(temp)
while (que):
    temp = que.pop(0)  # 取第一项
    for i in range(4):  # 四方向搜索
        nx = temp[0] + dx[i]
        ny = temp[1] + dy[i]
        if n > nx >= 0 and m > ny >= 0 and H[nx][ny] < H[temp[0]][temp[1]]:
            t = [nx, ny, temp[2] + 1]  # 新位置的信息
            que.append(t)  # 保存在list中
print(temp[2])  # 输出最后元素的路程
