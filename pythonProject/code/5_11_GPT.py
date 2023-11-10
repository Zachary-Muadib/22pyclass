def is_palindrome_slicing(s):
    # 使用字符串逆序切片方法
    return s == s[::-1]


def is_palindrome_for_loop(s):
    # 使用for循环逐字符比较
    length = len(s)
    for i in range(length // 2):
        if s[i] != s[length - 1 - i]:
            return False
    return True


def is_palindrome_list_reverse(s):
    # 将字符串转换为list后再利用列表的reverse()函数处理
    lst = list(s)
    lst.reverse()
    return s == ''.join(lst)


def is_palindrome_reversed(s):
    # 使用字符串的reversed()函数将字符反序
    return s == ''.join(reversed(s))


def is_palindrome_recursive(s):
    # 使用递归方法
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome_recursive(s[1:-1])


# 测试字符串
test_str = "bcba"
print("逆序切片方法:", is_palindrome_slicing(test_str))
print("for循环方法:", is_palindrome_for_loop(test_str))
print("list reverse方法:", is_palindrome_list_reverse(test_str))
print("reversed函数方法:", is_palindrome_reversed(test_str))
print("递归方法:", is_palindrome_recursive(test_str))

# 这道题输入输出你都要调整哦，输出这里你还要搞个小工具让True和False的判断结果变成中文的是和否进行输出
