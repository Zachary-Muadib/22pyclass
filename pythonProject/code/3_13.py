# 初始化用户输入的数字为非法值，以及两种方法的阶乘结果初始化为 1
n_input = float(-1)
n_factorial_for = 1
n_factorial_while = 1

# 使用 while 循环保证用户只能输入非负整数
while not (n_input.is_integer() and n_input >= 0):
    n_input = float(input("请输入非负整数n："))

# 将用户输入的浮点数转化为整数
n = int(n_input)
# 保存原始输入的值，供后续打印使用
n_origin = n

# 使用 for 循环计算 n 的阶乘
for i in range(1, n + 1):
    n_factorial_for = n_factorial_for * i
print(f"for循环： {n_origin}! = {n_factorial_for}")

# 使用 while 循环计算 n 的阶乘
while n > 0:
    n_factorial_while = n_factorial_while * n
    n = n - 1
print(f"while循环： {n_origin}! = {n_factorial_while}")
