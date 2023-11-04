import math

A = float(input("请输入直角三角形的直角边A（>0）:"))
B = float(input("请输入直角三角形的直角边B（>0）:"))

C = (A ** 2 + B ** 2) ** 0.5

L = A + B + C
S = A * B * 0.5

angleA = round(math.asin(A / C) * 180 / math.pi, 0)
angleB = round(math.asin(B / C) * 180 / math.pi, 0)

print(f"直角三角形三边分别为： a={A}，b={B}，c={C:.1f}")
print(str.format("三角形的周长={0:.1f},面积={1:.1f}", L, S))
print(f"三角形两个锐角的度数分别为： {angleA:.1f}° 和 {angleB:.1f}°")
