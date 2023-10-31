import math

a = 1
b = -10
c = 16

delta = b**2 - 4*a*c

if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"方程 x²-10x+16=0 的解为：{x1:.1f} {x2:.1f}")
elif delta == 0:
    x = -b / (2*a)
    print(f"方程 x²-10x+16=0 的解为：{x:.1f}")
else:
    print("方程 x²-10x+16=0 无解")
