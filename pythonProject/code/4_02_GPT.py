# 定义函数 generate_pascal_triangle，它接收一个参数 n，表示要生成杨辉三角的行数。
def generate_pascal_triangle(n):
    # 初始化结果列表。
    result = []
    # 对于 0 到 n-1 的每个 i，生成杨辉三角的一行。
    for i in range(n):
        if i == 0:
            # 如果是第一行，则直接添加包含数字1的列表。
            result.append([1])
        else:
            # 否则，获取上一行的数据。
            prev_line = result[-1]
            # 初始化当前行的列表，开始总是1。
            current_line = [1]
            # 遍历上一行的每个元素，除了最后一个，计算中间的值。
            for j in range(len(prev_line) - 1):
                # 当前元素等于上一行的两个相邻元素之和。
                current_line.append(prev_line[j] + prev_line[j + 1])
            # 每行的结尾也是1。
            current_line.append(1)
            # 将当前行添加到结果列表中。
            result.append(current_line)
    # 返回生成的杨辉三角。
    return result


# 定义函数 print_pascal_triangle，用于打印5行的杨辉三角。
def print_pascal_triangle():
    # 生成5行的杨辉三角。
    triangle = generate_pascal_triangle(5)
    # 设定打印的宽度。
    width = 20

    # 遍历杨辉三角的每一行。
    for line in triangle:
        # 将每个数字转换为字符串，然后用空格连接，最后居中对齐。
        print(' '.join(map(str, line)).center(width))


# 如果这个脚本是直接运行的，而不是作为模块导入，则执行以下代码。
if __name__ == "__main__":
    # 调用函数，打印杨辉三角。
    print_pascal_triangle()
