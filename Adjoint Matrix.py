import numpy as np

# 提示用户输入方阵维度
N = int(input("请输入方阵的维度N: "))

# 创建一个N*N的零矩阵
matrix = np.zeros((N, N), dtype=int)

print("请依次输入两位数字表示的矩阵位置，例如12代表第一行第二列，输入-1结束输入。")

while True:
    # 提示用户输入位置
    position = input("请输入位置: ")
    if position == "-1":
        break
    
    if len(position) == 2 and position.isdigit():
        row = int(position[0]) - 1
        col = int(position[1]) - 1
        
        if 0 <= row < N and 0 <= col < N:
            matrix[row][col] = 1
        else:
            print("输入的位置不在矩阵范围内，请重新输入。")
    else:
        print("输入无效，请输入两位数字。")

matrix = matrix.T

# 输出最终矩阵
print("最终矩阵 (Python 格式):")
print("np.array(")
print("    [")
for row in matrix:
    print("        [{0}],".format(", ".join(map(str, row))))
print("    ]")
print(")")

# 以MATLAB格式输出矩阵
print("MATLAB格式的矩阵输出:")
matlab_format = "; ".join([" ".join(map(str, row)) for row in matrix])
print(f"matrix = [{matlab_format}];")
