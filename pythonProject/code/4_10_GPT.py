def sqrt_newton(a):
    if a < 0:
        raise ValueError("输入必须是大于0的实数")
    elif a == 0:
        return 0
    # 初始猜测值为a的一半
    x = a / 2
    # 设置容忍误差
    tolerance = 1e-6
    while True:
        # 牛顿迭代公式
        next_x = (x + a / x) / 2
        # 检查当前迭代值与下一个迭代值的差的绝对值是否小于误差容限
        if abs(x - next_x) < tolerance:
            return round(next_x, 3)  # 保留三位小数并返回结果
        x = next_x


# 使用函数求平方根
A = float(input("请输入一个大于0的实数a："))
print("x的平方根是：", sqrt_newton(A))
