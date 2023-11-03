salary = float(input("请输入党员的月工资："))

if salary <= 3000:
    fee = salary * 0.005
elif salary <= 5000:
    fee = salary * 0.01
elif salary <= 10000:
    fee = salary * 0.015
else:
    fee = salary * 0.02

print(f"月工资 = {int(salary)}，交纳党费 = {int(fee)}")
