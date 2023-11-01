def delta(a, b, c):
    i = b ** 2 - 4 * a * c
    return i


def format_output(value):
    if isinstance(value, complex):
        real_part = value.real
        imag_part = value.imag
        return f"{format_output(real_part)} + {format_output(imag_part)}i"
    elif value.is_integer():
        return str(int(value))
    else:
        return f"{value:.4f}"


print("下面将求方程 ax²+bx+c=0 的解。")

A = float(input("请输入a的值："))
B = float(input("请输入b的值："))
C = float(input("请输入c的值："))
print("")

discriminant = delta(A, B, C)

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
        x1_result = (-B + 1j * discriminant ** 0.5) / (2 * A)
        x2_result = (-B - 1j * discriminant ** 0.5) / (2 * A)
        print(f"方程有两个共轭复根：\nx₁={format_output(x1_result)}\nx₂={format_output(x2_result)}")
