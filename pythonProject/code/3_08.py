print("Sn=1+1/2+1/3+...")
n = int(input("请输入n的值："))
Sn = 0

for i in range(1, n+1):
    x = 1 / i
    Sn = Sn + x

print(f"Sn={Sn:.4f}")
