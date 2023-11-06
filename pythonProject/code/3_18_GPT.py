from multiprocessing import Pool
from tqdm import tqdm


# 定义函数判断是否为自幂数
def is_armstrong(number):
    original = number
    power = len(str(number))
    sum_of_powers = 0
    while number > 0:
        number, digit = divmod(number, 10)  # 获取数字的最后一位并减少数字
        sum_of_powers += digit ** power  # 数字的各位数的幂次之和
    return sum_of_powers == original  # 判断是否为自幂数


# 在指定范围内查找所有的自幂数
def find_armstrong_numbers_in_range(range_tuple):
    start, end = range_tuple  # 获取范围的开始和结束
    found = []
    for number in range(start, end):
        if is_armstrong(number):  # 判断每个数字是否为自幂数
            found.append(number)
    return found


# 主函数
def main():
    cores = 30  # 使用的核心数
    range_per_core = 10 ** 7  # 每个核心处理的数字范围
    total_range = 10 ** 10  # 总的数字范围
    ranges = [(i, min(i + range_per_core, total_range)) for i in range(1, total_range, range_per_core)]
    all_armstrong_numbers = []
    # 使用多进程并行处理
    with Pool(cores) as pool:
        with tqdm(total=total_range) as pbar:  # 使用tqdm显示进度条
            for found in pool.imap_unordered(find_armstrong_numbers_in_range, ranges):
                pbar.update(range_per_core)  # 更新进度条
                all_armstrong_numbers.extend(found)  # 将找到的数字添加到列表中

    # 定义自幂数的名称
    name_map = {
        1: "独身数",
        3: "水仙花数",
        4: "四叶玫瑰数",
        5: "五角星数",
        6: "六合数",
        7: "北斗七星数",
        8: "八仙数",
        9: "九九重阳数",
        10: "十全十美数"
    }

    # 将找到的数字按位数分类
    classified_numbers = {}
    for num in all_armstrong_numbers:
        length = len(str(num))
        if length not in classified_numbers:
            classified_numbers[length] = []
        classified_numbers[length].append(num)

    # 打印分类后的数字
    for length, name in name_map.items():
        if length in classified_numbers:
            print(f"{name}{len(classified_numbers[length])}个：{' '.join(map(str, classified_numbers[length]))}")
        else:
            print(f"{name}没有自幂数！")


# 程序入口
if __name__ == "__main__":
    main()
