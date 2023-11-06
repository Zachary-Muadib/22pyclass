# 导入所需的模块
import sympy
import sys


# 定义一个函数来获取用户的整数输入，如果输入的不是整数，则会要求用户重新输入
def get_int_input(prompt):
    while True:
        value = input(prompt)
        try:
            return int(value)
        except ValueError:
            pass


# 初始化变量
foots = -1  # 脚的总数，初始化为-1，用于进入后面的while循环

# 获取用户输入的头的总数
heads = get_int_input("请输入总头数： ")

# 通过一个while循环确保用户输入的脚的总数是一个偶数
while foots % 2 != 0:
    foots = get_int_input("请输入总脚数（必须是偶数）： ")

# 检查输入是否有解，没有则退出程序
if heads * 2 > foots or heads * 4 < foots:
    sys.exit("方法一：无解，请重新运行测试！\n方法二：无解，请重新运行测试！\n方法三：无解，请重新运行测试！")

# 检查输入是否符合题目逻辑
if foots < heads * 2 or heads * 4 < foots:
    sys.exit("输入的头和脚的数量不符合逻辑，请重新运行测试！（没兔子怎么叫鸡兔同笼问题嘛（小声逼逼")

# 方法一：求解方程法
# 使用sympy库定义两个方程并求解
x1, y1 = sympy.symbols('x1, y1')
eq1 = sympy.Eq(x1 + y1, heads)
eq2 = sympy.Eq(2 * x1 + 4 * y1, foots)
solutions = sympy.solve((eq1, eq2), (x1, y1))

# 打印结果
print(f"方法一：鸡：{solutions[x1]}只，兔：{solutions[y1]}只")

# 方法二：公式法
# 根据头和脚的关系直接计算出鸡和兔的数量
y2 = 0.5 * foots - heads
x2 = heads - y2

# 打印结果
print(f"方法二：鸡：{int(x2)}只，兔：{int(y2)}只")

# 方法三：枚举法
# 初始化x3和y3
x3, y3 = 0, 0
# 通过枚举的方法找到符合条件的鸡和兔的数量
for x3 in range(0, heads + 1):
    y3 = heads - x3
    if 2 * x3 + 4 * y3 == foots:
        break

# 打印结果
print(f"方法三：鸡：{x3}只，兔：{y3}只")
