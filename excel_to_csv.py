"""
excle导出csv脚本(自动转utf8)
@author: ChenXing
@email:  onechenxing@163.com
@date:   2017/4/5

"""

from xlrd import *
import glob
import csv
def buildCsv(filePath):
    try:        
        data = open_workbook(filePath)
        sheet = data.sheet_by_index(0)
        csvFile = open(filePath[0:-5] + ".csv", "w", encoding = "utf-8", newline="")
        wr = csv.writer(csvFile,csv.excel)
        for i in range(0,sheet.nrows):
            row = sheet.row_values(i)
            #处理整数变成x.0的问题
            for v in range(0,len(row)):
                if type(row[v]) is float:
                    if row[v] % 1 == 0:
                        row[v] = int(row[v])
            wr.writerow(row)
        csvFile.close()
    except IOError as err:
        print("Error:" + str(err))
#导出csv目录下所有文件
csvFiles = glob.glob("csv\\*.xlsx")
for eachFile in csvFiles:
	buildCsv(eachFile)
	
print("excel_to_csv ok.")
#input()
