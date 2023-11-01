# 初始化阶乘结果为 1
factorial_result_for = 1
factorial_result_while = 1

# 使用 while 循环确保用户输入的是非负整数
while True:
    try:
        n = int(input("请输入非负整数n："))
        if n >= 0:
            break
        else:
            print("请输入一个非负整数!")
    except ValueError:
        print("输入无效，请输入一个非负整数!")

# 使用 for 循环计算 n 的阶乘
for i in range(1, n + 1):
    factorial_result_for *= i
print(f"for循环：{n}! = {factorial_result_for}")

# 使用 while 循环计算 n 的阶乘
num = n
while num > 0:
    factorial_result_while *= num
    num -= 1
print(f"while循环：{n}! = {factorial_result_while}")
