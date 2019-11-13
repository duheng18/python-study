import openpyxl, pprint

wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Population by Census Tract')
countData = {}

print('Reading rows...')
for row in range(2, sheet.max_row + 1):
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

    countData.setdefault(state, {})
    countData[state].setdefault(county, {'tracts': 0, 'pop': 0})
    countData[state][county]['tracts'] += 1
    countData[state][county]['pop'] = int(pop)

print('Writing results...')
resultFile = open('census2010.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countData))
resultFile.close()
print('Done.')
