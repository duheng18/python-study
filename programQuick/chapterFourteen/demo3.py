import csv

outputFile = open('output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)
# 21
print(outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham']))
# 31
print(outputWriter.writerow(['Hello,world!', 'eggs', 'bacon', 'ham']))
# 16
print(outputWriter.writerow([1, 2, 3.141592, 4]))
outputFile.close()
