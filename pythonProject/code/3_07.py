print("Sn=1-3+5-7+9-11+...")
n = int(input("请输入n的值："))
x = 1
Sn = 0

for i in range(n):
    Sn = Sn + ((-1)**(i % 2)) * x
    x = x + 2

print(f"Sn={Sn}")
