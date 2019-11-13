import openpyxl

wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')

# <Cell 'Sheet1'.A1>
print(sheet['A1'])

# 2015-04-05 13:34:02
print(sheet['A1'].value)

c = sheet['B1']
# Apples
print(c.value)

# Row 1, Column 2 is Apples
print('Row ' + str(c.row) + ', Column ' + str(c.column) + ' is ' + str(c.value))

# Cell B1 is Apples
print('Cell ' + c.coordinate + ' is ' + c.value)

# 73
print(sheet['C1'].value)
