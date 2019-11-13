import openpyxl

wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.get_active_sheet()
# <Worksheet "Sheet1">
# print(sheet)

# [(<Cell 'Sheet1'.A1>, <Cell 'Sheet1'.A2>, <Cell 'Sheet1'.A3>,
# <Cell 'Sheet1'.A4>, <Cell 'Sheet1'.A5>, <Cell 'Sheet1'.A6>,
# <Cell 'Sheet1'.A7>), (<Cell 'Sheet1'.B1>, <Cell 'Sheet1'.B2>,
# <Cell 'Sheet1'.B3>, <Cell 'Sheet1'.B4>, <Cell 'Sheet1'.B5>,
# <Cell 'Sheet1'.B6>, <Cell 'Sheet1'.B7>), (<Cell 'Sheet1'.C1>,
# <Cell 'Sheet1'.C2>, <Cell 'Sheet1'.C3>, <Cell 'Sheet1'.C4>,
# <Cell 'Sheet1'.C5>, <Cell 'Sheet1'.C6>, <Cell 'Sheet1'.C7>)]
# print(list(sheet.columns))
# 3
print(len(list(sheet.columns)))

for cell0 in list(sheet.columns)[0]:
    # 2015-04-05 13:34:02
    # 2015-04-05 03:41:23
    # 2015-04-06 12:46:51
    # 2015-04-08 08:59:43
    # 2015-04-10 02:07:00
    # 2015-04-10 18:10:37
    # 2015-04-10 02:40:46
    print(cell0.value)
for cell1 in list(sheet.columns)[1]:
    # Apples
    # Cherries
    # Pears
    # Oranges
    # Apples
    # Bananas
    # Strawberries
    print(cell1.value)

for cell2 in list(sheet.columns)[2]:
    # 73
    # 85
    # 14
    # 52
    # 152
    # 23
    # 98
    print(cell2.value)
