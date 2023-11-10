import pandas as pd
import matplotlib.pyplot as plt

# 设置matplotlib的字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为SimHei
plt.rcParams['axes.unicode_minus'] = False  # 解决负号问题

# Load the data from the Excel file
file_path = 'catering_sale.xls'  # 替换为您的Excel文件路径
sale_data = pd.read_excel(file_path)

# Create a boxplot to visualize the outliers
plt.figure(figsize=(10, 6))
bp = sale_data.boxplot(column=['销量'])

# 提取离群点
outliers = [flier.get_data()[1] for flier in bp.get_lines()[5:]]

# 标注离群点
for line in bp.get_lines()[5:]:
    y = line.get_ydata()
    x = line.get_xdata()
    for i in range(len(y)):
        plt.text(x[i], y[i], '%.2f' % y[i], ha='center', va='bottom', color='blue', fontsize=8)

plt.title('销量数据箱型图')
plt.ylabel('销量')
plt.grid(False)
plt.show()
