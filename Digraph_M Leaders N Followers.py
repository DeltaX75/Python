import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def numpy_to_matlab(matrix):
    """Convert a NumPy array to a MATLAB formatted string."""
    matlab_str = "["  # 开始 MATLAB 矩阵格式
    for row in matrix:
        # 将每一行转换为字符串，并用空格分隔元素
        row_str = " ".join(map(str, row))
        # 在 MATLAB 中，矩阵的行以分号隔开
        matlab_str += row_str + "; "
    matlab_str = matlab_str.strip("; ")  # 移除最后一个分号
    matlab_str += "]"  # 结束 MATLAB 矩阵格式
    return matlab_str

# 定义邻接矩阵，表示节点间的连接关系
A = np.array(
    [
        [0, 0, 0, 1],
        [1, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 1, 0],
    ]
)
# 将A的非0元素归一化
A[A != 0] = 1

receivers = [
    [1, 2],  # L1的接收者：1号、3号、5号、6号节点
    [4],  # L2的接收者：2号、4号节点
]

num_leaders = len(receivers)  # 自动获取领导者的数量

# 由于networkX邻接矩阵定义为i->j为1
# 因此我们需要转置一下
# 将矩阵转置以匹配networkX中的行为边的源节点，列为目标节点的约定
A = A.T

# 创建一个新的矩阵B，扩展原矩阵A以包含num_leaders个虚拟的领导者节点
B = np.zeros((A.shape[0] + num_leaders, A.shape[1] + num_leaders), dtype=int)
B[num_leaders:, num_leaders:] = (
    A  # 将A矩阵的内容填充到B中，不包括B的前num_leaders行和前num_leaders列
)

# 设置领导者到接收者的连接
for i, receiver_list in enumerate(receivers):
    for receiver in receiver_list:
        if receiver <= A.shape[0]:  # 检查接收者编号是否在原有节点范围内
            B[i, num_leaders + receiver - 1] = (
                1  # 领导者i连接到接收者receiver，考虑到编号偏移和领导者索引
            )


# 创建有向图对象
G = nx.from_numpy_array(B, create_using=nx.DiGraph)

# 设置节点位置
num_nodes = len(G)
num_followers = num_nodes - num_leaders  # 跟随者的数量
pos = {}
radius = 0.5  # 定义圆的半径
angle_increment = 2 * np.pi / num_nodes  # 计算角度增量

for i in range(num_nodes):
    angle = np.pi / 2 + i * angle_increment  # 从π/2 (90度)开始递增，实现逆时针布局
    pos[i] = (radius * np.cos(angle), radius * np.sin(angle))

# 绘制图，包括节点标签。使用自定义位置绘制节点
colors = ["#6495ED"] * num_leaders + ["#FFA07A"] * num_followers
labels = {
    i: f"L{i+1}" if i < num_leaders else f"{i+1-num_leaders}" for i in range(num_nodes)
}
nx.draw(
    G,
    pos,
    labels=labels,
    node_color=colors,
    edge_color="#909090",
    node_size=700,
    arrows=True,
    font_color="white",
)

# 设置坐标轴为1:1比例，防止图像被压扁或拉伸
plt.axis("equal")

# 输出矩阵信息区域

# 输出最终图的邻接矩阵
print("Adjacency Matrix =\n", B.T)
print("Adjacency Matrix =\n", numpy_to_matlab(B.T))
print("--------------------------------")

# 计算每个节点的入度（每行的和）
in_degrees = np.sum(B.T, axis=1)
# 创建入度矩阵 D，是一个对角矩阵，对角线元素为各节点的入度
D = np.diag(in_degrees)
# 计算拉普拉斯矩阵 L = D - A
L = D - B.T

# 输出图的拉普拉斯矩阵
print("Laplacian Matrix =\n", L)
print("Laplacian Matrix(Matlab) =\n", numpy_to_matlab(L))

# 保存图形
# plt.savefig('graph.svg', format='svg')
# 显示图形
plt.show()
