import os
import census2010

# {'pop': 291826, 'tracts': 55}
print(census2010.allData['AK']["Anchorage"])

anchoragePop=census2010.allData['AK']['Anchorage']['pop']

# The 2010 population of Anchorage was 291826
print('The 2010 population of Anchorage was '+str(anchoragePop))
