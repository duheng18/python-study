import openpyxl

wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')
# ((<Cell 'Sheet1'.A1>, <Cell 'Sheet1'.B1>, <Cell 'Sheet1'.C1>),
# (<Cell 'Sheet1'.A2>, <Cell 'Sheet1'.B2>, <Cell 'Sheet1'.C2>),
# (<Cell 'Sheet1'.A3>, <Cell 'Sheet1'.B3>, <Cell 'Sheet1'.C3>))
# print(tuple(sheet['A1':'C3']))
for rowOfCellObjects in sheet['A1':'C3']:
    for cellObj in rowOfCellObjects:
        # A1 2015-04-05 13:34:02
        # B1 Apples
        # C1 73
        # ---- END OF ROW ---
        # A2 2015-04-05 03:41:23
        # B2 Cherries
        # C2 85
        # ---- END OF ROW ---
        # A3 2015-04-06 12:46:51
        # B3 Pears
        # C3 14
        # ---- END OF ROW ---
        print(cellObj.coordinate, cellObj.value)
    print('---- END OF ROW ---')
