import openpyxl

wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.get_active_sheet()
print(list(sheet.columns)[1])
for cellObj in list(sheet.columns)[1]:
    print(cellObj.value)