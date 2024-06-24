import numpy as np

def matlab_to_numpy(matlab_str):
    # 去除方括号并按分号分割字符串以得到各行
    matlab_str = matlab_str.strip('[]')
    rows = matlab_str.split(';')
    
    # 处理每一行，格式化成Python适用的格式
    formatted_rows = []
    for row in rows:
        # 将每行按空格分割，然后用逗号连接
        formatted_row = ', '.join(row.split())
        formatted_rows.append('[' + formatted_row + ']')
    
    # 将所有格式化的行合并为一个字符串，表示为NumPy数组
    numpy_str = 'np.array([\n    ' + ',\n    '.join(formatted_rows) + '\n])'
    
    return numpy_str

# 请求用户输入MATLAB格式的矩阵
matlab_input = input("请输入MATLAB格式的矩阵. 例如：'[0 2 0; 2 0 -5; 0 5 0]': ")
numpy_output = matlab_to_numpy(matlab_input)
print("转换后的NumPy矩阵为:")
print(numpy_output)
