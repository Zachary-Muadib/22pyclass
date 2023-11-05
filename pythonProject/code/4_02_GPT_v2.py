# 初始化存储结果的列表
result = [[1]]

# 外层循环，遍历帕斯卡三角形的每一行
for i in range(1, 5):
    # 使用列表推导式根据帕斯卡三角形的规律计算当前行
    current = [1] + [result[i-1][j] + result[i-1][j+1] for j in range(i-1)] + [1]
    # 将当前行添加到结果列表中
    result.append(current)

# 打印帕斯卡三角形
for row in result:
    print(' '.join(map(str, row)).center(20))
