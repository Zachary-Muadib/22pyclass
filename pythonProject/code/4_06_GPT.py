def simple_arithmetic_calculator(num1, num2, opr):
    if num2 == 0 and opr in ('/', '%'):
        raise ValueError("分母=0，零除异常！")
    if opr == '+':
        result = num1 + num2
    elif opr == '-':
        result = num1 - num2
    elif opr == '*':
        result = num1 * num2
    elif opr == '/':
        result = num1 / num2
    elif opr == '%':
        result = num1 % num2
    else:
        raise ValueError("无效操作符！")
    return f"{num1} {opr} {num2} = {result}"


# 主程序部分
# 提示用户输入第一个操作数，并将输入转换为浮点数。
x = float(input("请输入操作数x："))
# 提示用户输入第二个操作数，并将输入转换为浮点数。
y = float(input("请输入操作数y："))
# 提示用户输入操作符。
operator = input("请输入操作符：")

# 调用simple_arithmetic_calculator函数，并打印结果。
print(simple_arithmetic_calculator(x, y, operator))
