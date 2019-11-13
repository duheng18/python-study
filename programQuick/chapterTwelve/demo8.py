import openpyxl

wb = openpyxl.Workbook()
# ['Sheet']
print(wb.get_sheet_names())
sheet = wb.get_active_sheet()
# sheet
print(sheet.title)

sheet.title = 'Spam Bacon Eggs Sheet'
# ['Spam Bacon Eggs Sheet']
print(wb.get_sheet_names())

wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.get_active_sheet()
sheet.title = 'Spam Spam Spam'
wb.save('example_copy.xlsx')
