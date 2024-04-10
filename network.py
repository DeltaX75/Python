import matplotlib.pyplot as plt
import networkx as nx

# 定义邻接矩阵
A = [
  [0, 0, 0, 1],
  [1, 0, 0, 0],
  [0, 0, 0, 1],
  [0, 1, 1, 0]
]

# 创建有向图
G = nx.DiGraph()

# 添加节点，节点编号从1开始
G.add_nodes_from([1, 2, 3, 4])

# 根据邻接矩阵A添加边，注意索引与节点编号之间的关系
for i in range(len(A)):
    for j in range(len(A[i])):
        if A[i][j] == 1:
            # 节点编号是从1开始的，因此在添加边时要将索引加1以匹配节点编号
            G.add_edge(i+1, j+1)

# 绘制图
nx.draw(G, with_labels=True, node_color='skyblue', node_size=700, arrowstyle='-|>', arrowsize=12)
plt.show()
