import openpyxl
from openpyxl.styles import Font

wb = openpyxl.Workbook()
sheet = wb.get_sheet_by_name('Sheet')

footObj1 = Font(name='Times New Roman', bold=True)
sheet['A1'].font = footObj1
sheet['A1'] = 'Bold Times New Roman'

footObj2 = Font(size=24, italic=True)
sheet['B3'].font = footObj2
sheet['B3'] = '24 pt Itali'

wb.save('styles.xlsx')
