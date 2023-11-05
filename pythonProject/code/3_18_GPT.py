# 导入必要的模块
from multiprocessing import Pool
from tqdm import tqdm


# 判断一个数是否是阿姆斯特朗数
def is_armstrong(number):
    original = number
    power = len(str(number))  # 计算数字的位数
    sum_of_powers = 0
    # 循环，计算每一位数字的power次方之和
    while number > 0:
        number, digit = divmod(number, 10)
        sum_of_powers += digit ** power
    # 如果次方和与原数相等，则是阿姆斯特朗数
    return sum_of_powers == original


# 在一个范围内找出所有的阿姆斯特朗数
def find_armstrong_numbers_in_range(range_tuple):
    start, end = range_tuple
    found = []
    # 遍历指定范围的每一个数字
    for number in range(start, end):
        if is_armstrong(number):
            found.append(number)
    return found


# 主函数
def main():
    # 设置核心数量和每个核心处理的范围
    cores = 8
    range_per_core = 10 ** 6
    total_range = 10 ** 10

    # 创建每个核心处理的范围的列表
    ranges = [(i, min(i + range_per_core, total_range)) for i in range(1, total_range, range_per_core)]

    all_armstrong_numbers = []

    # 使用多进程处理
    with Pool(cores) as pool:
        # 使用tqdm展示处理进度
        with tqdm(total=total_range) as pbar:
            for found in pool.imap_unordered(find_armstrong_numbers_in_range, ranges):
                pbar.update(range_per_core)
                all_armstrong_numbers.extend(found)

    # 打印找到的阿姆斯特朗数的数量和列表
    print(f"Total Armstrong numbers found: {len(all_armstrong_numbers)}")
    print(f"Armstrong numbers: {all_armstrong_numbers}")


# 当直接运行此脚本时执行主函数
if __name__ == "__main__":
    main()
