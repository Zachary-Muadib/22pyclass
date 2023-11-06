# 获取用户输入的实数x
x = float(input("请输入一个实数："))

# 初始化泰勒级数的第一项值为1（对应于0的阶乘）
term_value = 1

# 初始化结果为0
result = 1

# 初始化n，它将用于表示当前项的索引
n = 1

# 初始化n的阶乘的值为1（0的阶乘为1）
n_factorial = 1

# 当前项的值大于1e-6时继续循环
# 1e-6是一个非常小的数，用于判断当前项的值是否足够小以至于可以忽略
while abs(term_value) >= 1e-6:
    result += term_value  # 将当前项的值累加到结果中
    n += 1  # 将n增加1，移动到下一项
    n_factorial *= n  # 计算n的阶乘
    term_value = (x ** n) / n_factorial  # 根据泰勒级数的公式计算下一项的值

# 打印e^x的近似值，保留两位小数
print(f"e^x的近似值为{result:.2f}")
