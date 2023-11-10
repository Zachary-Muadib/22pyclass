import pandas as pd

file_path = 'catering_sale.xls'
sale_data = pd.read_excel(file_path)

sales_descriptive_stats = sale_data['销量'].describe()

print(sales_descriptive_stats)
