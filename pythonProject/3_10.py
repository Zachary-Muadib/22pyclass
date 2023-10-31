def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a


def triangle_perimeter(a, b, c):
    return a + b + c


def triangle_area(a, b, c):
    h = triangle_perimeter(a, b, c) / 2
    return (h * (h - a) * (h - b) * (h - c)) ** 0.5


A = float(input("请输入三角形的边A："))
B = float(input("请输入三角形的边B："))
C = float(input("请输入三角形的边C："))

if is_triangle(A, B, C):
    L = triangle_perimeter(A, B, C)
    S = triangle_area(A, B, C)
    print(f"三角形三边分别为：a={A:.1f}，b={B:.1f}，c={C:.1f}")
    print(f"三角形的周长 = {L:.1f}，面积 = {S:.1f}")
else:
    print("\033[91m无法构成三角形！\033[0m")
