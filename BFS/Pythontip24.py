# https://blog.csdn.net/marxoffice/article/details/97501536
n = 10
m = 3

map = [[100000000 for x in range(m + 1)] for y in range(n + 1)]
used = [[0 for x in range(m + 1)] for y in range(n + 1)]
map[0][0] = 0
dx = [1, -1, 1, -1, 2, -2, 2, -2]
dy = [2, -2, -2, 2, 1, -1, -1, 1]  # 八个扩展方向
horses = []
horses.append([0, 0])
while (horses):
    h = horses[0]  # 取出第一项
    del horses[0]  # 删除第一项
    if h[0] == n and h[1] == m:  # 已达终点
        break
    for i in range(8):  # 八个方向探索
        nx = h[0] + dx[i]
        ny = h[1] + dy[i]
        if nx >= 0 and nx <= n and ny >= 0 and ny <= m and used[nx][ny] == 0:
            map[nx][ny] = map[h[0]][h[1]] + 1  # 记录长度
            used[nx][ny] = 1  # 已经使用
            horses.append([nx, ny])  # 将该点保存在list中
if map[n][m] != 100000000:
    print(map[n][m])
else:
    print(-1)
