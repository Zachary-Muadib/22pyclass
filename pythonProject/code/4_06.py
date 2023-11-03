def calculator(num1, num2, opr):
    if opr == '+':
        result = num1 + num2
    elif opr == '-':
        result = num1 - num2
    elif opr == '*':
        result = num1 * num2
    elif opr == '/':
        if num2 == 0:
            return "分母=0，零除异常！"
        else:
            result = num1 / num2
    elif opr == '%':
        if num2 == 0:
            return "分母=0，零除异常！"
        else:
            result = num1 % num2
    else:
        return "无效操作符！"
    return f"{num1} {opr} {num2} = {result}"


x = float(input("请输入操作数x："))
y = float(input("请输入操作数y："))
operator = input("请输入操作符：")

print(calculator(x, y, operator))
