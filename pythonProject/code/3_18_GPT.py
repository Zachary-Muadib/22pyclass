from multiprocessing import Pool
from tqdm import tqdm


# 判断一个数是否是阿姆斯特朗数
def is_armstrong(number):
    original = number
    power = len(str(number))
    sum_of_powers = 0
    while number > 0:
        number, digit = divmod(number, 10)
        sum_of_powers += digit ** power
    return sum_of_powers == original


# 在一个范围内找出所有的阿姆斯特朗数
def find_armstrong_numbers_in_range(range_tuple):
    start, end = range_tuple
    found = []
    for number in range(start, end):
        if is_armstrong(number):
            found.append(number)
    return found


# 主函数
def main():
    cores = 30
    range_per_core = 10 ** 7
    total_range = 10 ** 10
    ranges = [(i, min(i + range_per_core, total_range)) for i in range(1, total_range, range_per_core)]
    all_armstrong_numbers = []
    with Pool(cores) as pool:
        with tqdm(total=total_range) as pbar:
            for found in pool.imap_unordered(find_armstrong_numbers_in_range, ranges):
                pbar.update(range_per_core)
                all_armstrong_numbers.extend(found)

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

    classified_numbers = {}
    for num in all_armstrong_numbers:
        length = len(str(num))
        if length not in classified_numbers:
            classified_numbers[length] = []
        classified_numbers[length].append(num)

    for length, name in name_map.items():
        if length in classified_numbers:
            print(f"{name}{len(classified_numbers[length])}个：{' '.join(map(str, classified_numbers[length]))}")
        else:
            print(f"{name}没有自幂数！")


# 当直接运行此脚本时执行主函数
if __name__ == "__main__":
    main()
