# 输入工资
salary = float(input("请输入党员的月工资: "))

# 计算党费
if salary <= 3000:
    fee = salary * 0.005
elif 3000 < salary <= 5000:
    fee = salary * 0.01
elif 5000 < salary <= 10000:
    fee = salary * 0.015
else:
    fee = salary * 0.02

# 输出结果
print(f"月工资 = {int(salary):d}，交纳党费 = {int(fee):d}")
