input_str = str(input("请输入字符串："))

total_char = 0
alpha_count = 0
digit_count = 0
space_count = 0
other_count = 0

for char in input_str:
    total_char += 1
    if char.isalpha():
        alpha_count += 1
    elif char.isdigit():
        digit_count += 1
    elif char.isspace():
        space_count += 1
    else:
        other_count += 1

print(f"所有字母的总数为：{total_char}\n"
      f"英文字母出现的次数：{alpha_count}\n"
      f"数字出现的次数：{digit_count}\n"
      f"空格出现的次数：{space_count}\n"
      f"其他字符出现的次数：{other_count}")
