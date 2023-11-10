s = [9, 7, 8, 3, 2, 1, 5, 6]

print(s)

# 遍历列表
for i in range(len(s)):
    if s[i] % 2 == 0:  # 检查元素是否为偶数
        s[i] = s[i] ** 2  # 将偶数替换为其平方

print(s)

# 这个输出你也要调整一下
