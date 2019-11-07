# 使用*字段宽度说明符来格式化一张包含水果价格的表格，表格的总宽度由用户输入。
# 使用给定的宽度打印格式化后的价格列表
width = eval(input('Please enter width:'))
price_width = 10
item_width = width - price_width
# print(item_width)
header_format = '%-*s%*s'
format = '%-*s%*.2f'
print('=' * width)
print(header_format % (item_width, 'Item', price_width, 'Price'))
print('-' * width)
print(format % (item_width, 'Apples', price_width, 0.4))
print(format % (item_width, 'Pears', price_width, 0.5))
print(format % (item_width, 'Cantaloupes', price_width, 1.92))
print(format % (item_width, 'Dried Apricots(160z.)', price_width, 8))
print(format % (item_width, 'Prunes(4 lbs.)', price_width, 12))
print('=' * width)
# 22
# ================================
# Item                       Price
# --------------------------------
# Apples                      0.40
# Pears                       0.50
# Cantaloupes                 1.92
# Dried Apricots(160z.)       8.00
# Prunes(4 lbs.)             12.00
# ================================
