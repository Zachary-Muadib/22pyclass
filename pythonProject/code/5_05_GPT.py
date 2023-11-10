# 定义一个列表
numbers = [9, 7, 8, 3, 2, 1, 55, 6]

# 方法一：使用for循环
count1, max1, min1, sum1 = 0, None, None, 0
for number in numbers:
    count1 += 1
    sum1 += number
    if max1 is None or number > max1:
        max1 = number
    if min1 is None or number < min1:
        min1 = number
avg1 = sum1 / count1 if count1 else 0

# 方法二：使用while循环
count2, max2, min2, sum2, i = 0, None, None, 0, 0
while i < len(numbers):
    number = numbers[i]
    count2 += 1
    sum2 += number
    if max2 is None or number > max2:
        max2 = number
    if min2 is None or number < min2:
        min2 = number
    i += 1
avg2 = sum2 / count2 if count2 else 0

# 方法三：使用for循环和range
count3, max3, min3, sum3 = 0, None, None, 0
for i in range(len(numbers)):
    number = numbers[i]
    count3 += 1
    sum3 += number
    if max3 is None or number > max3:
        max3 = number
    if min3 is None or number < min3:
        min3 = number
avg3 = sum3 / count3 if count3 else 0

# 方法四：使用while True循环
count4, max4, min4, sum4, i = 0, None, None, 0, 0
while True:
    if i >= len(numbers):
        break
    number = numbers[i]
    count4 += 1
    sum4 += number
    if max4 is None or number > max4:
        max4 = number
    if min4 is None or number < min4:
        min4 = number
    i += 1
avg4 = sum4 / count4 if count4 else 0

# 方法五：使用内置函数
count5 = len(numbers)
max5 = max(numbers) if numbers else None
min5 = min(numbers) if numbers else None
sum5 = sum(numbers)
avg5 = sum5 / count5 if count5 else 0

# 打印结果
print("方法一：", count1, max1, min1, sum1, avg1)
print("方法二：", count2, max2, min2, sum2, avg2)
print("方法三：", count3, max3, min3, sum3, avg3)
print("方法四：", count4, max4, min4, sum4, avg4)
print("方法五：", count5, max5, min5, sum5, avg5)

# 这道题输出这个地方你可能大概要调整一下哦
