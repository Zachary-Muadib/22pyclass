import random

# 产生三个0~100的随机数
a = random.randint(0, 100)
b = random.randint(0, 100)
c = random.randint(0, 100)

print(f"原始值: {a}, {b}, {c}")

# 方法一: 比较法
if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b
print(f"（方法一）升序值: {a}, {b}, {c}")

# 方法二: 使用max()、min()函数
min_num = min(a, b, c)
max_num = max(a, b, c)
mid_num = a + b + c - min_num - max_num
print(f"（方法二）升序值: {min_num}, {mid_num}, {max_num}")

# 方法三: 使用列表的sorted()函数
sorted_list = sorted([a, b, c])
print(f"（方法三）升序值: {sorted_list[0]}, {sorted_list[1]}, {sorted_list[2]}")
