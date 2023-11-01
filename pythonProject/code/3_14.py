import math
import random

random1 = int(random.randint(0, 100))
random2 = int(random.randint(0, 100))

# gcd()函数求最大公约数
gcd = math.gcd(random1)

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
