import math

# 输入直角三角形的两个直角边
a = float(input("请输入直角三角形的直角边A(>0)："))
b = float(input("请输入直角三角形的直角边B(>0)："))

# 计算斜边
c = math.sqrt(a ** 2 + b ** 2)

# 输出三角形的三边长
print(f"直角三角形三边分别为： a={a:.1f}，b={b:.1f}，c={c:.1f}")

# 计算三角形的周长和面积
p = a + b + c
area = 0.5 * a * b

# 利用math.asin和math.acos函数计算三角形的两个锐角的度数
sinA = a / c
cosA = b / c
angleA = round(math.asin(sinA) * 180 / math.pi, 1)
angleB = round(math.acos(cosA) * 180 / math.pi, 1)

# 输出三角形的周长和面积以及两个锐角的度数
print(str.format("三角形的周长={0:1.1f}, 面积={1:1.1f}", p, area))
print(f"三角形的两个锐角度数分别为： {angleA:.1f}° 和 {angleB:.1f}°")
