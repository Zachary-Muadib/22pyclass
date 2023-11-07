input_str = str(input("请输入字符串："))

# 使用 split() 分割字符串，得到单词列表
words = input_str.split()

# 使用 len() 获取列表长度，即单词数量
n = len(words)

print(f"其中的单词总数有：{n}")
