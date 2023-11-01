import datetime

sName = input("请输入您的姓名：")
birth_year = int(input("请输入您的出生年份："))

current_year = datetime.date.today().year
age = current_year - birth_year

print("您好！{0}。您{1}岁。".format(sName, age))
