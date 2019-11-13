
import openpyxl

wbFormulas=openpyxl.load_workbook('writeFormula.xlsx')
sheet=wbFormulas.get_active_sheet()
# =SUM(A1:A2)
print(sheet['A3'].value)

weDataOnly=openpyxl.load_workbook('writeFormula.xlsx',data_only=True)
sheet=weDataOnly.get_active_sheet()
print(sheet['A3'].value)