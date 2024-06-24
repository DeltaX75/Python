import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# 定义邻接矩阵，表示节点间的连接关系
A = np.array([
    [0, 0, 0, 2, 1, 0],
    [1, 0, 0, 0, 0, 0],
    [0, 3, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 0, 0, 1, 0]
])

# 创建一个新的矩阵B，扩展原矩阵A以包含一个虚拟的0号节点
B = np.zeros((A.shape[0] + 1, A.shape[1] + 1), dtype=int)
B[1:, 1:] = A  # 将A矩阵的内容填充到B中，不包括B的第一行和第一列

# 假设接收消息的节点索引，指定哪些节点可以接收0号节点的消息
receivers = [1, 3, 4]  # 1号、3号、4号节点接收0号节点的消息

# 初始化B矩阵的第一行和第一列为零
B[0, :] = 0
B[:, 0] = 0

# 设置第一列中，可以接收消息的节点的位置为1，表示这些节点与0号节点有联系
B[receivers, 0] = 1

# 由于NetworkX从numpy矩阵创建图时，矩阵的行代表边的源节点，列代表边的目标节点
# 因此我们需要将矩阵转置
B = B.T

# 创建有向图对象
G = nx.from_numpy_array(B, create_using=nx.DiGraph)

# 设置节点位置
num_nodes = len(G)
pos = {}
radius = 0.5  # 定义圆的半径
angle_increment = 2 * np.pi / num_nodes  # 计算角度增量

for i in range(num_nodes):
    angle = np.pi / 2 + i * angle_increment  # 从π/2 (90度)开始递增，实现逆时针布局
    pos[i] = (radius * np.cos(angle), radius * np.sin(angle))

# 绘制图，包括节点标签。使用自定义位置绘制节点
nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='#909090', node_size=700, arrows=True)

# 设置坐标轴为1:1比例，防止图像被压扁或拉伸
plt.axis('equal')

# 显示图形
plt.show()
