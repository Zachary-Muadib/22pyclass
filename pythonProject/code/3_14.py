import math
import random

random1 = int(random.randint(0, 100))
random2 = int(random.randint(0, 100))
print(f"整数1 = {random1}", end="，")
print(f"整数2 = {random2}")

# gcd()函数求最大公约数
gcd = math.gcd(random1, random2)
print(f"最大公约数 = {gcd}")

# 辗转相除法求最大公约数
if random1 == random2:
    gcd = random1
else:
    if random1 > random2:
        m = random1
        n = random2
    else:
        m = random2
        n = random1
    while m % n != 0:
        m, n = n, m % n
    gcd = n
print(f"最大公约数 = {gcd}")

# 更相减损法求最大公约数
m = random1
n = random2
while m != n:
    if m > n:
        m = m - n
    else:
        n = n - m
gcd = m
print(f"最大公约数 = {gcd}")

# lcm()函数求最小公倍数
lcm = math.lcm(random1, random2)
print(f"最小公倍数 = {lcm}")

# 公式求最小公倍数
lcm = random1 * random2 // gcd
print(f"最小公倍数 = {lcm}")
