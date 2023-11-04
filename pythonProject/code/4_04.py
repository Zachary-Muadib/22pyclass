import random

a = random.randint(0, 100)
b = random.randint(0, 100)
c = random.randint(0, 100)

print(f"原始值： a={a}， b={b}， c={c}")

# 方法一
a_min_1 = a if a < b else b
a_min = a_min_1 if a_min_1 < c else c
if a_min == a:
    a_max = b if b > c else c
elif a_min == b:
    a_max = a if a > c else c
else:
    a_max = a if a > b else b
a_mid = a + b + c - a_min - a_max
print(f"（方法一）升序值： a={a_min}， b={a_mid}， c={a_max}")

# 方法二
b_min = min(a, b, c)
b_max = max(a, b, c)
b_mid = a + b + c - b_min - b_max
print(f"（方法二）升序值： a={b_min}， b={b_mid}， c={b_max}")

# 方法三
nums = [a, b, c]
sorted_nums = sorted(nums)
print(f"（方法三）升序值： a={sorted_nums[0]}， b={sorted_nums[1]}， c={sorted_nums[2]}")
