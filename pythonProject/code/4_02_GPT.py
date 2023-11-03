def generate_pascal_triangle(n):
    """生成n行的杨辉三角"""
    result = []
    for i in range(n):
        if i == 0:
            result.append([1])
        else:
            prev_line = result[-1]
            current_line = [1]  # 每行的开始都是1
            for j in range(len(prev_line) - 1):
                current_line.append(prev_line[j] + prev_line[j + 1])
            current_line.append(1)  # 每行的结束都是1
            result.append(current_line)
    return result


def print_pascal_triangle():
    """格式化打印5行的杨辉三角"""
    triangle = generate_pascal_triangle(5)
    width = 20  # 固定每行的宽度为20个字符

    for line in triangle:
        # 将每一行转化为字符串并居中对齐
        print(' '.join(map(str, line)).center(width))


if __name__ == "__main__":
    print_pascal_triangle()
