import openpyxl

wb = openpyxl.Workbook()
sheet = wb.get_active_sheet()
for i in range(1, 11):
    sheet['A' + str(i)] = i

refObj = openpyxl.Reference(sheet, (1, 1), (10, 1))
seriesObj = openpyxl.charts.Series(refObj, title='First series')
chartObj=openpyxl
