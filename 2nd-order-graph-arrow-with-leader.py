import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# 定义邻接矩阵
A = np.array([
    [0, 0, 0, 2, 1, 0],
    [1, 0, 0, 0, 0, 0],
    [0, 3, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 0, 0, 1, 0]
])

# 创建一个新的矩阵B，初始化为零，大小为原矩阵A的行数+1，列数+1
B = np.zeros((A.shape[0] + 1, A.shape[1] + 1), dtype=int)
B[1:, 1:] = A

# 假设接收消息的节点索引
receivers = [1, 3, 4]  # 假设1号、3号、4号节点可以接收0号节点的消息

# 初始化第一行和第一列为零
B[0, :] = 0
B[:, 0] = 0

# 设置可以接收消息的节点在第一列
B[receivers, 0] = 1

# 将矩阵转置以匹配networkX中的行为边的源节点，列为目标节点的约定
B = B.T

# 创建有向图对象
G = nx.from_numpy_array(B, create_using=nx.DiGraph)

# 设置节点位置
num_nodes = len(G)
pos = {}
leader_distance = 1.5  # 设置领导者（节点0）离圆心的距离
angle_offset = np.pi / 8  # 增加一个角度偏移来避免直线对齐
for i in range(1, num_nodes):
    angle = 2 * np.pi * (i - 1) / (num_nodes - 1) + angle_offset
    pos[i] = (np.cos(angle), np.sin(angle))  # 逆时针布局，调整角度计算
pos[0] = (np.cos(np.pi + angle_offset), leader_distance)  # 将0号节点放在圆的外侧正下方

# 绘制图，包括节点标签
nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='#909090', node_size=700, arrows=True)

# 显示图
plt.show()
