# 定义一个函数来计算二次方程的判别式
def delta(a, b, c):
    return b ** 2 - 4 * a * c


# 定义一个函数来格式化输出的结果：如果结果是整数则不显示小数部分，否则显示4位小数
def format_output(value):
    # 检查是否为复数
    if isinstance(value, complex):
        # 分离复数的实部和虚部
        real_part = value.real
        imag_part = value.imag
        # 分别格式化实部和虚部
        return f"{format_output(real_part)} + {format_output(imag_part)}i"
    # 检查数字是否为整数
    elif value.is_integer():
        return str(int(value))
    else:
        return f"{value:.4f}"


# 主程序开始
print("下面将求方程 ax²+bx+c=0 的解。")

# 从用户输入获取二次方程的系数
A = float(input("请输入a的值："))
B = float(input("请输入b的值："))
C = float(input("请输入c的值："))

# 计算判别式的值
discriminant = delta(A, B, C)

# 根据系数和判别式的值来判断方程的根的情况
if A == 0 and B == 0:
    print("方程无解")
elif A == 0 and B != 0:
    x_result = -C / B
    print(f"方程有一个实数根：\nx={format_output(x_result)}")
else:
    if discriminant == 0:
        x_result = -B / (2 * A)
        print(f"方程有两个相等实根：\nx₁=x₂={format_output(x_result)}")
    elif discriminant > 0:
        x1_result = (-B + discriminant ** 0.5) / (2 * A)
        x2_result = (-B - discriminant ** 0.5) / (2 * A)
        print(f"方程有两个不等实根：\nx₁={format_output(x1_result)}\nx₂={format_output(x2_result)}")
    else:
        # 如果判别式小于0，方程有复根
        x1_result = (-B + 1j * discriminant ** 0.5) / (2 * A)
        x2_result = (-B - 1j * discriminant ** 0.5) / (2 * A)
        print(str(f"方程有两个共轭复根：\nx₁={format_output(x1_result)}\nx₂={format_output(x2_result)}").replace('j', 'i'))
