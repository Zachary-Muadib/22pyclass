def split_number(n, position):
    return (n % (10**position)) // (10**(position-1))


num = int(input("请输入一个三位自然数："))

# 使用整除运算符//和求余数（求模）运算符%
a1 = num // 100
a2 = num % 100 // 10
a3 = num % 10
print(f"方法一： {a1} {a2} {a3}")

# 使用divmod()函数
tup = divmod(num, 100)
b1 = tup[0]
b2, b3 = divmod(tup[1], 10)
print(f"方法二： {b1} {b2} {b3}")

# 使用map()函数
positions = [3, 2, 1]
c1, c2, c3 = map(lambda p: split_number(num, p), positions)
print(f"方法三： {c1} {c2} {c3}")
