import openpyxl

wb = openpyxl.load_workbook('example.xlsx')

# <class 'openpyxl.workbook.workbook.Workbook'>
# print(type(wb))

# ['Sheet1', 'Sheet2', 'Sheet3']
# print(wb.get_sheet_names())

sheet = wb.get_sheet_by_name('Sheet3')

# <Worksheet "Sheet3">
# print(sheet)

# <class 'openpyxl.worksheet.worksheet.Worksheet'>
# print(type(sheet))

# Sheet3
# print(sheet.title)

anotherSheet = wb.get_active_sheet()
# <Worksheet "Sheet1">
print(anotherSheet)
