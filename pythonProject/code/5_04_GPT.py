# 获取用户输入的列表，元素用空格分隔
input_str = input("请输入列表，用空格分隔每个元素：")
input_list = input_str.split()

# 初始化一个空集合，用于存放已遇到的唯一元素
seen = set()

# 初始化一个空列表，用于存放结果
output_list = []

# 遍历输入列表
for item in input_list:
    # 如果当前元素不在已遇到的集合中，添加到集合和输出列表中
    if item not in seen:
        seen.add(item)
        output_list.append(item)

print("去重后的列表：", output_list)
