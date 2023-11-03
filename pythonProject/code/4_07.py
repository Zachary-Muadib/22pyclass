def classify_triangle(a, b, c):
    # 检查是否能构成三角形
    if (a + b > c) and (a + c > b) and (b + c > a):
        # 检查是否为等边三角形
        if a == b == c:
            return "该三角形为等边三角形！"
        # 检查是否为等腰三角形
        elif a == b or a == c or b == c:
            return "该三角形为等暖三角形！"
        # 检查是否为直角三角形
        elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            return "该三角形为直角三角形！"
        else:
            return "该三角形为普通三角形！"
    else:
        return "无法构成三角形！"


# 输入三角形的三条边
A = float(input("请输入三角形的边a："))
B = float(input("请输入三角形的边b："))
C = float(input("请输入三角形的边c："))

# 输出检查结果
print(classify_triangle(A, B, C))
