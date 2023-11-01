def calculate_right_triangle_hypotenuse(a, b):
    c = (a ** 2 + b ** 2) ** 0.5
    return c


A = float(input("请输入直角三角形的直角边1（>0）："))
B = float(input("请输入直角三角形的直角边2（>0）："))

hypotenuse = calculate_right_triangle_hypotenuse(A, B)

print("直角三角形的斜边为：%.2f" % hypotenuse)
