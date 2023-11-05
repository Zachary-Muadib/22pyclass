# 初始化存储结果的列表
result = []

# 外层循环，遍历帕斯卡三角形的每一行
for i in range(1, 6):
    # 如果是第一行，只添加一个元素1
    if i == 1:
        result.append([1])
    # 其他行的处理
    else:
        # 获取上一行的数据
        last = result[-1]
        # 当前行的开头是1
        current = [1]
        # 内层循环，计算当前行的中间元素
        j = 2
        while i > 2 and j < i:
            # 根据帕斯卡三角形的规律计算元素值
            current.append(last[j - 2] + last[j - 1])
            j = j + 1
        # 当前行的结尾是1
        current.append(1)
        # 将当前行添加到结果列表中
        result.append(current)

# 打印帕斯卡三角形
for row in result:
    print(' '.join(map(str, row)).center(20))
