import math


def piecewise_f_right(a):
    return (a ** 2 - 3 * a) / (a + 1) + 2 * math.pi + math.sin(a)


def piecewise_f_left(a):
    return math.log(-5 * a) + 6 * (abs(a) + math.e ** 4) ** 0.5 - (a + 1) ** 3


x = float(input("请输入x："))
y = 0

print("方法一:", end="")
if x >= 0:
    y = piecewise_f_right(x)
if x < 0:
    y = piecewise_f_left(x)
print(f"x = {x:.1f}，y = {y:.14f}")

print("方法二:", end="")
if x >= 0:
    y = piecewise_f_right(x)
else:
    y = piecewise_f_left(x)
print(f"x = {x:.1f}，y = {y:.14f}")

print("方法三:", end="")
y = piecewise_f_right(x) if x >= 0 else piecewise_f_left(x)
print(f"x = {x:.1f}，y = {y:.14f}")
