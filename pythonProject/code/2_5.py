def getValue(b, r, n):
    v = b * (1 + r)**n
    return v


B = float(input("请输入本金："))
R = float(input("请输入年利率："))
N = float(input("请输入年数："))

V = getValue(B, R, N)

print(f"最终收益为：{V:.2f}")
