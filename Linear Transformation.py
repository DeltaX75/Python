import math
import numpy as np
import matplotlib.pyplot as plt

# 定义变换矩阵
A = np.array([[4, -1], [1, 2]])

if __name__ == "__main__":
    # 原始点集
    points = np.array([[0, 0], [0, 5], [3, 5], [3, 4], [1, 4],
                       [1, 3], [2, 3], [2, 2], [1, 2], [1, 0]])
    
    # 应用矩阵变换
    transformed_points = np.dot(points, A)
    
    # 提取原始点的x和y坐标
    x_original = points[:, 0]
    y_original = points[:, 1]

    # 提取变换后的x和y坐标
    x_transformed = transformed_points[:, 0]
    y_transformed = transformed_points[:, 1]

# 绘图设置
plt.figure(figsize=(5,5))
plt.xlim(-10, 20)
plt.ylim(-10, 20)

# 绘制原始点
# plt.plot(x_original, y_original, 'bo-', label='Original Points')  # 蓝色圆点和线
plt.plot(x_original, y_original, label='Original Points')  # 蓝色圆点和线
# 绘制变换后的点
plt.plot(x_transformed, y_transformed, label='Transformed Points')  # 红色圆点和线

# 绘制坐标轴箭头
# plt.annotate('', xy=(20, 0), xytext=(0, 0), arrowprops=dict(facecolor='black', shrink=0.00))
# plt.annotate('', xy=(0, 20), xytext=(0, 0), arrowprops=dict(arrowstyle='->', facecolor='black'))


# 绘制坐标轴
plt.axhline(0, color='black', linewidth=1)  # 水平x轴
plt.axvline(0, color='black', linewidth=1)  # 垂直y轴
# 添加图例
plt.legend()

# 显示图形
plt.show()
