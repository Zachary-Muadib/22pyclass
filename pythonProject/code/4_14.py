import random

# 随机生成1到10之间的整数n
n = random.randint(1, 10)
# 初始化结果为0
result = 0
# 初始化当前项为0
current = 0

# 循环n次，从1到n
for i in range(1, n + 1):
    # 当前项是之前的项加上10的i-1次方
    current += 10 ** (i - 1)
    # 累加当前项到结果
    result += current

# 打印n和数列的和
print(f"n = {n}, Sn = {result}")
