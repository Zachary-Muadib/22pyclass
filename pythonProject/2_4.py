import math


def calculate_sphere_surface_area(r):
    s = 4 * math.pi * r**2
    return s


def calculate_sphere_volume(r):
    v = 4 / 3 * math.pi * r**3
    return v


R = float(input("请输入球的半径："))

S = calculate_sphere_surface_area(R)
V = calculate_sphere_volume(R)

print("球的表面积为：%.2f，体积为：%.2f" % (S, V))
# print("球的表面积为:{0:.2f}，体积为:{1:.2f}".format(S, V))
# print(f"球的表面积为:{S:.2f}，体积为:{V:.2f}")
