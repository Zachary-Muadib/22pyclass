def calculate_compound_interest(p, r, t):
    a = p * (1 + r / 100) ** t
    return a


P = float(input("请输入本金："))
R = float(input("请输入年利率（%）："))
T = float(input("请输入年份："))

A = calculate_compound_interest(P, R, T)

print("本金利率和为：%.2f" % A)
