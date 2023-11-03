# 定义一个名为calculator的函数，它接收三个参数：num1, num2和opr。
# num1和num2是进行运算的数，opr是一个字符串，表示运算符。
def calculator(num1, num2, opr):
    # 检查opr是否为加号('+')，如果是，则执行加法。
    if opr == '+':
        result = num1 + num2
    # 如果opr是减号('-')，执行减法。
    elif opr == '-':
        result = num1 - num2
    # 如果opr是乘号('*')，执行乘法。
    elif opr == '*':
        result = num1 * num2
    # 如果opr是除号('/')，执行除法。
    elif opr == '/':
        # 在执行除法前，检查第二个操作数（分母）是否为零。
        if num2 == 0:
            return "分母=0，零除异常！"
        else:
            result = num1 / num2
    # 如果opr是取余符号('%')，执行取余运算。
    elif opr == '%':
        # 在执行取余运算前，检查第二个操作数（分母）是否为零。
        if num2 == 0:
            return "分母=0，零除异常！"
        else:
            result = num1 % num2
    # 如果opr不是上述任何一个运算符，则返回无效操作符提示。
    else:
        return "无效操作符！"
    # 格式化输出运算结果，并将其返回。
    return f"{num1} {opr} {num2} = {result}"


# 主程序部分
# 提示用户输入第一个操作数，并将输入转换为浮点数。
x = float(input("请输入操作数x："))
# 提示用户输入第二个操作数，并将输入转换为浮点数。
y = float(input("请输入操作数y："))
# 提示用户输入操作符。
operator = input("请输入操作符：")

# 调用calculator函数，并打印结果。
print(calculator(x, y, operator))
